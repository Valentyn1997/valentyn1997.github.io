---
title: "Orthogonal Learner for Estimating Heterogeneous Long-Term Treatment Effects"
collection: projects
authors: 'H. Ma, D. Frauen, <b>V. Melnychuk</b>, S. Feuerriegel'
date: 2026-04-01
excerpt: "![lo-dr](/images/lo-dr.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2604.00915'
preprint: true
---

Estimation of heterogeneous long-term treatment effects (HLTEs) is relevant for personalized decision-making in marketing, economics, and medicine, where short-term observational datasets are often combined with long-term observational datasets. However, HLTE estimation is challenging due to limited overlap in treatment assignments or in long-term outcomes for certain subpopulations, which can lead to unstable HLTE estimates with large finite-sample variance. To address this challenge, we introduce the LT-O-learners (Long-Term Orthogonal Learners), a set of novel orthogonal learners for HLTE estimation in the canonical HLTE setting with surrogacy. The key idea of our LT-O-learners is to retarget the loss via custom overlap weights that downweight low-overlap samples. We show that the retargeted loss recovers the true HLTE pointwise and satisfies Neyman-orthogonality. We further prove two key theoretical results: (i) The nuisance error enters the error bound only through higher-order terms, which means our learners are robust to nuisance estimation error. (ii) Under a linear function class, the retargeting effectively controls the asymptotic variance of the HLTE estimator via the overlap weights in low-overlap regimes. We conduct experiments on synthetic and real-world datasets to confirm the theoretical properties of our LT-O-learners, particularly robustness in low-overlap regimes. To our knowledge, ours are the first orthogonal learners for HLTE estimation robust to low overlap in long-term settings.

Recommended citation: 
```bibtex
@article{ma2026orthogonal,
  title={Orthogonal Learner for Estimating Heterogeneous Long-Term Treatment Effects},
  author={Ma, Haorui and Frauen, Dennis and Melnychuk, Valentyn and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2604.00915},
  year={2026}
}
```
