---
title: "Frequentist Consistency of Prior-Data Fitted Networks for Causal Inference"
collection: publications
authors: '<b>V. Melnychuk</b>, V. Balazadeh, S. Feuerriegel, R. G Krishnan'
date: 2026-03-12
excerpt: "![pfns-freq](/images/pfns-freq.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2603.12037'
preprint: true
---

Foundation models based on prior-data fitted networks (PFNs) have shown strong empirical performance in causal inference by framing the task as an in-context learning this http URL, it is unclear whether PFN-based causal estimators provide uncertainty quantification that is consistent with classical frequentist estimators. In this work, we address this gap by analyzing the frequentist consistency of PFN-based estimators for the average treatment effect (ATE). (1) We show that existing PFNs, when interpreted as Bayesian ATE estimators, can exhibit prior-induced confounding bias: the prior is not asymptotically overwritten by data, which, in turn, prevents frequentist consistency. (2) As a remedy, we suggest employing a calibration procedure based on a one-step posterior correction (OSPC). We show that the OSPC helps to restore frequentist consistency and can yield a semi-parametric Bernstein-von Mises theorem for calibrated PFNs (i.e., both the calibrated PFN-based estimators and the classical semi-parametric efficient estimators converge in distribution with growing data size). (3) Finally, we implement OSPC through tailoring martingale posteriors on top of the PFNs. In this way, we are able to recover functional nuisance posteriors from PFNs, required by the OSPC. In multiple (semi-)synthetic experiments, PFNs calibrated with our martingale posterior OSPC produce ATE uncertainty that (i) asymptotically matches frequentist uncertainty and (ii) is well calibrated in finite samples in comparison to other Bayesian ATE estimators.

Recommended citation: 
```bibtex
@article{melnychuk2026frequentist,
  title={Frequentist Consistency of Prior-Data Fitted Networks for Causal Inference},
  author={Melnychuk, Valentyn and Balazadeh, Vahid and Feuerriegel, Stefan and Krishnan, Rahul G.},
  journal={arXiv preprint arXiv:2603.12037},
  year={2026}
}
```
