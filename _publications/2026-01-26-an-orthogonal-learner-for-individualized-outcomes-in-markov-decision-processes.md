---
title: "An Orthogonal Learner for Individualized Outcomes in Markov Decision Processes"
collection: publications
authors: 'E. Javurek, <b>V. Melnychuk</b>, J. Schweisthal, K. Hess, D. Frauen, S. Feuerriegel'
date: 2026-01-26
excerpt: "![fair-policy](/images/orth-mdp.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/2509.26429'
venue: 'ICLR'
paperurl: 'https://openreview.net/pdf?id=PRu8Sybp1j'
---

Predicting individualized potential outcomes in sequential decision-making is central for optimizing therapeutic decisions in personalized medicine (e.g., which dosing sequence to give to a cancer patient). However, predicting potential out- comes over long horizons is notoriously difficult. Existing methods that break the curse of the horizon typically lack strong theoretical guarantees such as orthogonality and quasi-oracle efficiency. In this paper, we revisit the problem of predicting individualized potential outcomes in sequential decision-making (i.e., estimating Q-functions in Markov decision processes with observational data) through a causal inference lens. In particular, we develop a comprehensive theoretical foundation for meta-learners in this setting with a focus on beneficial theoretical properties. As a result, we yield a novel meta-learner called DRQ-learner and establish that it is: (1) doubly robust (i.e., valid inference under model misspecification), (2) Neyman-orthogonal (i.e., insensitive to first-order estimation errors in the nuisance functions), and (3) achieves quasi-oracle efficiency (i.e., behaves asymptotically as if the ground-truth nuisance functions were known). Our DRQ-learner is applicable to settings with both discrete and continuous state spaces. Further, our DRQ-learner is flexible and can be used together with arbitrary machine learning models (e.g., neural networks). We validate our theoretical results through numerical experiments, thereby showing that our meta-learner outperforms state-of-the-art baselines.


Recommended citation: 
```bibtex
@inproceedings{javurek2026orthogonal,
  title={An Orthogonal Learner for Individualized Outcomes in Markov Decision Processes},
  author={Javurek, Emil and Melnychuk, Valentyn and Schweisthal, Jonas, and Hess, Konstantin and Frauen, Dennis and Feuerriegel, Stefan},
  booktitle={International Conference on Learning Representations},
  year={2026}
}
```
