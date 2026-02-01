---
title: "Orthogonal Representation Learning for Estimating Causal Quantities"
collection: publications
authors: '<b>V. Melnychuk</b>, D. Frauen, J. Schweisthal, S. Feuerriegel'
date: 2026-01-22
excerpt: "![orht-repr](/images/orht-repr.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2502.04274'
venue: 'AISTATS'
kind: 'oral presentation'
---

End-to-end representation learning has become a powerful tool for estimating causal quantities from high-dimensional observational data, but its efficiency remained unclear. Here, we face a central tension: End-to-end representation learning methods often work well in practice but lack asymptotic optimality in the form of the quasi-oracle efficiency. In contrast, two-stage Neyman-orthogonal learners provide such a theoretical optimality property but do not explicitly benefit from the strengths of representation learning. In this work, we step back and ask two research questions: (1) When do representations strengthen existing Neyman-orthogonal learners? and (2) Can a balancing constraint – commonly proposed technique in the representation learning literature – provide improvements to Neyman-orthogonality? We address these two questions through our theoretical and empirical analysis, where we introduce a unifying framework that connects representation learning with Neyman-orthogonal learners (namely, OR-learners). In particular, we show that, under the low-dimensional manifold hypothesis, the OR-learners can strictly improve the estimation error of the standard Neyman-orthogonal learners. At the same time, we find that the balancing constraint requires an additional inductive bias and cannot generally compensate for the lack of Neyman-orthogonality of the end-to-end approaches. Building on these insights, we offer guidelines for how users can effectively combine representation learning with the classical Neyman-orthogonal learners to achieve both practical performance and theoretical guarantees.

Recommended citation: 
```bibtex
@inproceedings{melnychuk2026orthogonal,
  title={Orthogonal representation learning for estimating causal quantities},
  author={Melnychuk, Valentyn and Frauen, Dennis and Schweisthal, Jonas and Feuerriegel, Stefan},
  booktitle={International Conference on Artificial Intelligence and Statistics},
  year={2026}
}
```
