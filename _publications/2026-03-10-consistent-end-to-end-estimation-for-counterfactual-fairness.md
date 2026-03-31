---
title: "Consistent End-to-End Estimation for Counterfactual Fairness"
collection: publications
authors: 'Y. Ma*, <b>V. Melnychuk*</b>, D. Frauen, S. Feuerriegel'
date: 2026-03-10
excerpt: "![fair-policy](/images/gan-fairness.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2310.17687'
venue: 'CLeaR'
paperurl: 'https://openreview.net/pdf?id=aCCkuwjaH6'
kind: 'poster'
code: 'https://github.com/yccm/consistent-estimation-gcfn'
---

Counterfactual fairness seeks to ensure that the prediction for an individual is the same as that in a counterfactual world under a different sensitive attribute. However, achieving counterfactual fairness in practice is challenging due to several issues. In this paper, we discuss two key issues and suggest workarounds for them. (1) Counterfactual fairness involves counterfactual quantities, which rely on unobservable outcomes and inference and which require additional, non-trivial counterfactual identifiability assumptions. Here, we explicitly state the counterfactual identifiability assumptions necessary to guarantee point identification of counterfactuals up to a measure-preserving indeterminacy (MPI). Without such counterfactual identifiability assumptions, counterfactual fairness can not be reliably fulfilled, even with infinite data. (2) Even assuming counterfactual identifiability holds, many existing baselines for counterfactual fairness lack consistency in estimating counterfactuals and thus may yield predictions that are unfair. In our work, we redefine the notion of consistency so that it (i) is compatible with the counterfactual identifiability up to an MPI, and (ii) allows to enforce worst-case counterfactual fairness. Following this definition of consistency, we develop an end-to-end method that allows for consistent estimation of counterfactuals (which we call generative counterfactual fairness network). Once the counterfactuals are consistently estimated, we can use regularization as an in-processing approach to enforce the worst-case counterfactual fairness in prediction models. With our work, we aim to spur a discussion of when and where counterfactual fairness can be reliably achieved to ensure a safe and ethical use. 

Recommended citation: 
```bibtex
@inproceedings{ma2026consistent,
    title={Consistent End-to-End Estimation for Counterfactual Fairness},
    author={Yuchen Ma and Valentyn Melnychuk and Dennis Frauen and Stefan Feuerriegel},
    booktitle={Conference on Causal Learning and Reasoning},
    year={2026},
}
```
