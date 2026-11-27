---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Employment
* Postdoctoral researcher, LMU Munich, Germany, 2026 - Present

## Education
* Ph.D. in Computer Science, LMU Munich, Germany, 2021 - 2026
* M.S. in Data Science, LMU Munich, Germany, 2018 - 2021
* B.S. in System Analysis, National Technical University of Ukraine ”Igor Sikorsky Kyiv Polytechnic Institute”, Ukraine, 2014 - 2018

## Publications
### Peer-reviewed
{% assign current_year = '' %}
<ul>
  {% for post in site.publications reversed %}
    {% if post.preprint != true %}
      {% assign pub_year = post.date | date: "%Y" %}
      {% if pub_year != current_year %}
        <h3>{{ pub_year }}</h3>
        {% assign current_year = pub_year %}
      {% endif %}
      {% include archive-single-cv.html %}
    {% endif %}
  {% endfor %}
</ul>

### Pre-prints
<ul>
{% for post in site.projects reversed %}
  {% if post.preprint %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>
  
## Talks
{% assign current_year = '' %}
<ul>{% for post in site.talks reversed %}
  {% assign talk_year = post.date | date: "%Y" %}
  {% if talk_year != current_year %}
    <h3>{{ talk_year }}</h3>
    {% assign current_year = talk_year %}
  {% endif %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>

## Academic activities
* Reviewer at [ICML 2024](https://icml.cc/Conferences/2024), [ICML 2025](https://icml.cc/Conferences/2025), [ICML 2026](https://icml.cc/Conferences/2026) (gold)
* Reviewer at [ICLR 2024](https://iclr.cc/Conferences/2024), [ICLR 2025](https://iclr.cc/Conferences/2025), [ICLR 2026](https://iclr.cc/Conferences/2026), [ICLR 2027](https://iclr.cc/Conferences/2027)
* Reviewer at [NeurIPS 2023](https://nips.cc/Conferences/2023) (top), [NeurIPS 2024](https://nips.cc/Conferences/2024), [NeurIPS 2025](https://nips.cc/Conferences/2025), [NeurIPS 2026](https://nips.cc/Conferences/2026) (top), 
* Reviewer at [AISTATS 2023](http://www.aistats.org/aistats2023/) (top), [AISTATS 2024](https://aistats.org/aistats2024/), [AISTATS 2026](https://aistats.org/aistats2026/), [AISTATS 2027](https://aistats.org/aistats2027/)
* Research stay at [Rahul G. Krishnan's Lab](https://www.cs.toronto.edu/~rahulgk/) at the University of Toronto & Vector Institute, Oct-Dec 2025
* Mentor at the [Responsible AI for Ukraine 2025 program](https://airesponsibly.net/RAIforUkraine/)
* Research stay at [van der Schaar Lab](https://www.vanderschaar-lab.com/) at the University of Cambridge, Feb-May 2024
* Teacher assistant at [Nordic Probabilistic AI School 2023](https://probabilistic.ai/)

## Work experience
* Research Assistant, Fraunhofer Institute for Integrated Circuits IIS (Munich, Germany), 2019 - 2021
* Intern Data Scientist, Beehiveor Academy and R&D Labs (Kyiv, Ukraine), 2018
* Junior Java Developer, ProFIX (Kyiv, Ukraine), 2017 - 2018
  
## Awards & Affiliations
* Director of the [Causal ML Lab](https://www.som.lmu.de/ai/en/research/causal-ml-lab/) at the Institute of AI in Management, LMU Munich, since 2024
* [Associated PhD student](https://zuseschoolrelai.de/people/scientists/valentyn-melnychuk/) at Konrad Zuse School of Excellence in Reliable AI (relAI), 2023 - 2026
* LMU Study Scholarship for International Students, 2019
* Ukrainian Team Programming Olympiad, 2016

## Languages
* English - C1.2+
* German - C1.2
* Ukrainian - native speaker

## Volunteer Activity 
* Volunteer, NGO "Agency For Free Development" (Kyiv, Ukraine), 2016 - 2018
* Member / activist, IASA Student Council (Kyiv, Ukraine), 2015 - 2016