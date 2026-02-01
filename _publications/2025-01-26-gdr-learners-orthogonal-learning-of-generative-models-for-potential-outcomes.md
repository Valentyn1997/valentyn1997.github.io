---
title: "GDR-learners: Orthogonal Learning of Generative Models for Potential Outcomes"
collection: publications
authors: '<b>V. Melnychuk</b>, S. Feuerriegel'
date: 2025-09-26
excerpt: "![gdr](/images/gdr.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2509.22953'
venue: 'ICLR'
---

Various deep generative models have been proposed to estimate potential outcomes distributions from observational data. However, none of them have the favorable theoretical property of general Neyman-orthogonality and, associated with it, quasi-oracle efficiency and double robustness. In this paper, we introduce a general suite of generative Neyman-orthogonal (doubly-robust) learners that estimate the conditional distributions of potential outcomes. Our proposed generative doubly-robust learners (GDR-learners) are flexible and can be instantiated with many state-of-the-art deep generative models. In particular, we develop GDR-learners based on (a) conditional normalizing flows (which we call GDR-CNFs), (b) conditional generative adversarial networks (GDR-CGANs), (c) conditional variational autoencoders (GDR-CVAEs), and (d) conditional diffusion models (GDR-CDMs). Unlike the existing methods, our GDR-learners possess the properties of quasi-oracle efficiency and rate double robustness, and are thus asymptotically optimal. In a series of (semi-)synthetic experiments, we demonstrate that our GDR-learners are very effective and outperform the existing methods in estimating the conditional distributions of potential outcomes.


Recommended citation: 
```bibtex
@inproceedings{melnychuk2026gdrlearners,
  title={GDR-learners: Orthogonal Learning of Generative Models for Potential Outcomes},
  author={Melnychuk, Valentyn and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2026}
}
```
