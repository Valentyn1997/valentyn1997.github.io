---
title: "IGC-Net for Conditional Average Potential Outcome Estimation over Time"
collection: publications
authors: 'K. Hess, D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2026-01-26
excerpt: "![fair-policy](/images/g-transfromer.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2405.21012'
venue: 'ICLR'
paperurl: 'https://openreview.net/pdf?id=ZmhpqpKzAT'
kind: 'poster'
---

Estimating potential outcomes for treatments over time based on observational data is important for personalized decision-making in medicine. However, many existing methods for this task fail to properly adjust for time-varying confounding and thus yield biased estimates. There are only a few neural methods with proper adjustments, but these have inherent limitations (e.g., division by propensity scores that are often close to zero), which result in poor performance. As a remedy, we introduce the iterative G-computation network (IGC-Net). Our IGC-Net is a novel, neural end-to-end model which adjusts for time-varying confounding in order to estimate conditional average potential outcomes (CAPOs) over time. Specifically, our IGC-Net is the first neural model to perform fully regression-based iterative G-computation for CAPOs in the time-varying setting. We evaluate the effectiveness of our IGC-Net across various experiments. In sum, this work represents a significant step towards personalized decision-making from electronic health records.


Recommended citation: 
```bibtex
@inproceedings{hess2026igc,
  title={IGC-Net for conditional average potential outcome estimation over time},
  author={Hess, Konstantin and Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2026}
}
```
