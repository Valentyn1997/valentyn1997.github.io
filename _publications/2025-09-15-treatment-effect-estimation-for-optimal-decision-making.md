---
title: "Treatment Effect Estimation for Optimal Decision-Making"
collection: publications
authors: 'D. Frauen, <b>V. Melnychuk</b>, J. Schweisthal, M. van der Schaar, S. Feuerriegel'
date: 2025-09-15
excerpt: "![treat-pol](/images/treat-pol.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2505.13092'
venue: 'NeurIPS'
kind: 'poster'
---

Decision-making across various fields, such as medicine, heavily relies on conditional average treatment effects (CATEs). Practitioners commonly make decisions by checking whether the estimated CATE is positive, even though the decision-making performance of modern CATE estimators is poorly understood from a theoretical perspective. In this paper, we study optimal decision-making based on two-stage CATE estimators (e.g., DR-learner), which are considered state-of-the-art and widely used in practice. We prove that, while such estimators may be optimal for estimating CATE, they can be suboptimal when used for decision-making. Intuitively, this occurs because such estimators prioritize CATE accuracy in regions far away from the decision boundary, which is ultimately irrelevant to decision-making. As a remedy, we propose a novel two-stage learning objective that retargets the CATE to balance CATE estimation error and decision performance. We then propose a neural method that optimizes an adaptively-smoothed approximation of our learning objective. Finally, we confirm the effectiveness of our method both empirically and theoretically. In sum, our work is the first to show how state-of-the-art CATE estimators can be adapted for optimal decision-making.

Recommended citation: 
```bibtex
@inproceedings{frauen2025treatment,
  title={Treatment Effect Estimation for Optimal Decision-Making},
  author={Frauen, Dennis and Melnychuk, Valentyn and Schweisthal, Jonas and van der Schaar, Mihaela and Feuerriegel, Stefan},
  booktitle={Advances in Neural Information Processing Systems},
  year={2025}
}
```
