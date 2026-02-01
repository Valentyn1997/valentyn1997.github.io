---
title: "Overlap-Adaptive Regularization for Conditional Average Treatment Effect Estimation"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, J. Schweisthal, S. Feuerriegel'
date: 2026-01-26
excerpt: "![oar](/images/oar.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2509.24962'
venue: 'ICLR'
paperurl: 'https://openreview.net/pdf?id=HMMSnGgYOy'
kind: 'poster'
---

The conditional average treatment effect (CATE) is widely used in personalized medicine to inform therapeutic decisions. However, state-of-the-art methods for CATE estimation (so-called meta-learners) often perform poorly in the presence of low overlap. In this work, we introduce a new approach to tackle this issue and improve the performance of existing meta-learners in the low-overlap regions. Specifically, we introduce Overlap-Adaptive Regularization (OAR) that regularizes target models proportionally to overlap weights so that, informally, the regularization is higher in regions with low overlap. To the best of our knowledge, our OAR is the first approach to leverage overlap weights in the regularization terms of the meta-learners. Our OAR approach is flexible and works with any existing CATE meta-learner: we demonstrate how OAR can be applied to both parametric and non-parametric second-stage models. Furthermore, we propose debiased versions of our OAR that preserve the Neyman-orthogonality of existing meta-learners and thus ensure more robust inference. Through a series of (semi-)synthetic experiments, we demonstrate that our OAR significantly improves CATE estimation in low-overlap settings in comparison to constant regularization.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2026overlap,
  title={Overlap-Adaptive Regularization for Conditional Average Treatment Effect Estimation},
  author={Melnychuk, Valentyn and Frauen, Dennis and Schweisthal, Jonas and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2026}
}
```
