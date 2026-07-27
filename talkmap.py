# # Leaflet cluster map of talk locations
#
# Originally (c) 2016-2017 R. Stuart Geiger, released under the MIT license.
# Rewritten to drop the abandoned `getorg` / `geopy` dependencies -- this now
# uses only the standard library and talks directly to Nominatim.
#
# Run from the repository root:  python3 talkmap.py
#
# It mines the `location` field from each _talks/*.md file, geocodes the distinct
# values with Nominatim, and writes talkmap/org-locations.js, which
# talkmap/map.html reads to render the cluster map.

import glob
import json
import re
import sys
import time
import urllib.parse
import urllib.request

# Locations that cannot be placed on a map.
SKIP = {"online"}

# Nominatim's usage policy requires an identifying User-Agent and at most
# 1 request/second. This runs rarely and over a handful of places, so be polite.
USER_AGENT = "valentyn1997.github.io-talkmap/1.0 (melnychuk@lmu.de)"
RATE_LIMIT_S = 1.2

# Nominatim has no entry for some venues; fall back to a coarser query but keep
# the talk's own location string as the marker label.
FALLBACKS = {
    "Vector Institute, Toronto, Canada": "Toronto, Ontario, Canada",
}


def geocode(query):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": query, "format": "json", "limit": 1}
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        results = json.load(resp)
    return results[0] if results else None


def collect_locations():
    """Distinct `location` values across _talks/*.md, in file order."""
    locations = []
    for path in sorted(glob.glob("_talks/*.md")):
        with open(path, encoding="utf-8") as f:
            match = re.search(r'^location:\s*"(.*?)"', f.read(), re.M)
        if not match:
            print("  no location field, skipping: %s" % path)
            continue
        location = match.group(1).strip()
        if location.lower() in SKIP:
            continue
        if location not in locations:
            locations.append(location)
    return locations


def main():
    locations = collect_locations()
    print("%d distinct mappable location(s)" % len(locations))

    points, failed = [], []
    for location in locations:
        result = geocode(location)
        if result is None and location in FALLBACKS:
            print("  %r not found, trying fallback %r" % (location, FALLBACKS[location]))
            time.sleep(RATE_LIMIT_S)
            result = geocode(FALLBACKS[location])
        if result is None:
            print("  FAILED to geocode %r" % location)
            failed.append(location)
        else:
            points.append([location, float(result["lat"]), float(result["lon"])])
            print("  %r -> %s, %s" % (location, result["lat"], result["lon"]))
        time.sleep(RATE_LIMIT_S)

    if not points:
        sys.exit("no locations could be geocoded; leaving org-locations.js untouched")

    body = ",\n".join(
        '  [\n    "%s",\n    %s,\n    %s\n  ]' % (name, lat, lon)
        for name, lat, lon in points
    )
    with open("talkmap/org-locations.js", "w", encoding="utf-8") as f:
        f.write("var addressPoints = [\n" + body + "\n];")

    print("wrote talkmap/org-locations.js with %d marker(s)" % len(points))
    if failed:
        print("NOT on the map (geocoding failed): %s" % ", ".join(failed))


if __name__ == "__main__":
    main()
