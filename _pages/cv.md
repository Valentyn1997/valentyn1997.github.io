---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education
* Ph.D. in Computer Science, LMU Munich, Germany, 2021 - Present
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
{% for post in site.publications reversed %}
  {% if post.preprint %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>
  
## Talks
<ul>{% for post in site.talks reversed %}
{% include archive-single-talk-cv.html %}
{% endfor %}</ul>

## Academic activities
* Reviewer at [ICML 2025](https://icml.cc/Conferences/2025)
* Reviewer at [ICLR 2025](https://iclr.cc/Conferences/2025)
* Reviewer at [NeurIPS 2024](https://nips.cc/Conferences/2024)
* Reviewer at [ICML 2024](https://icml.cc/Conferences/2024)
* Research stay at [van der Schaar Lab](https://www.vanderschaar-lab.com/) at the University of Cambridge, Feb-May 2024
* Reviewer at [AISTATS 2024](https://aistats.org/aistats2024/)
* Reviewer at [ICLR 2024](https://iclr.cc/Conferences/2024)
* Top reviewer at [NeurIPS 2023](https://nips.cc/Conferences/2023)
* Teacher assistant at [Nordic Probabilistic AI School 2023](https://probabilistic.ai/)
* Top reviewer at [AISTATS 2023](http://www.aistats.org/aistats2023/)

## Work experience
* Research Assistant, Fraunhofer Institute for Integrated Circuits IIS (Munich, Germany), 2019 - 2021
* Intern Data Scientist, Beehiveor Academy and R&D Labs (Kyiv, Ukraine), 2018
* Junior Java Developer, ProFIX (Kyiv, Ukraine), 2017 - 2018
  
## Awards & Affiliations
* Co-director of the [Causal ML Lab](https://www.som.lmu.de/ai/en/research/causal-ml-lab/) at the Institute of AI in Management, LMU Munich, since 2024
* [Associated PhD student](https://zuseschoolrelai.de/people/scientists/valentyn-melnychuk/) at Konrad Zuse School of Excellence in Reliable AI (relAI), since 2023
* LMU Study Scholarship for International Students, 2019
* Ukrainian Team Programming Olympiad, 2016

## Languages
* English - C1.2+
* German - C1.1
* Ukrainian - native speaker

## Volunteer Activity 
* Volunteer, NGO "Agency For Free Development" (Kyiv, Ukraine), 2016 - 2018
* Member / activist, IASA Student Council (Kyiv, Ukraine), 2015 - 2016