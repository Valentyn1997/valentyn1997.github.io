---
title: "ConfoundingSHAP: Quantifying Confounding Strength in Causal Inference"
collection: projects
authors: 'M. Brockschmidt, S. M. A. R. Thies, M. Schröder, D. Frauen, <b>V. Melnychuk</b>, M. Muschalik, E. Hüllermeier, S. Feuerriegel'
date: 2026-05-11
excerpt: "![confounding-shap](/images/confounding-shap.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2605.10533'
preprint: true
---

In causal inference, confounders are variables that influence both treatment decisions and outcomes. However, unlike as in randomized clinical trials, the treatment assignment mechanism in observational studies is not known, and it is thus unclear which covariates act as confounders. Here, we aim to generate insight for causal inference and answer: which of the observed covariates act as confounders? We introduce ConfoundingSHAP, a Shapley-based method for attributing confounding strength to individual covariates. Our contributions are twofold. First, we propose a Shapley game targeted to infer the confounding strength of the covariates. Our resulting Shapley values differ from the standard applications of SHAP explanations on causal targets, such as understanding treatment effect heterogeneity, which are ill-suited for our task. Second, as our task requires evaluating the value function over many adjustment sets, we provide a scalable TabPFN-based estimation that avoids exhaustive refitting. We demonstrate the practical value across various datasets, where ConfoundingSHAP provides informative explanations of which observed covariates drive confounding and thereby helps to provide more insight for causal inference in practice.

Recommended citation: 
```bibtex
@article{brockschmidt2026confoundingshap,
  title={Confounding{SHAP}: Quantifying Confounding Strength in Causal Inference},
  author={Brockschmidt, Marie and Thies, Santo M. A. R. and Schr{\"o}der, Maresa and Frauen, Dennis and Melnychuk, Valentyn and Muschalik, Maximilian and H{\"u}llermeier, Eyke and Feuerriegel, Stefan},
  journal={arXiv preprint arXiv:2605.10533},
  year={2026}
}
```
