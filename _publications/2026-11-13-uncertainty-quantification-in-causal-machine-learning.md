---
title: "Uncertainty Quantification in Causal Machine Learning"
collection: publications
authors: '<b>V. Melnychuk</b>'
date: 2026-11-13
venue: 'LMU Munich'
kind: 'PhD dissertation'
excerpt: ""
paperurl: 'https://edoc.ub.uni-muenchen.de/37918/1/melnychuk_valentyn.pdf'
---

Causal machine learning (causal ML) integrates structural causal knowledge with flexible predictive models to estimate the consequences of interventions from observational data. A central goal is treatment effect estimation – learning how an outcome would change under alternative actions (treatments), either on average or as a whole distribution. The estimates of treatment effects then underpin data-driven decision making in settings where randomized trials are limited or infeasible. These settings include personalized medicine (selecting therapies for patients), public policy (evaluating program impacts), marketing (forecasting responses to pricing or outreach), and education (targeting interventions to students).

Reliable decision-making from observational data requires not only estimating treatment effects but also quantifying the uncertainty that surrounds them. In the context of the causal ML, three main sources of uncertainty can be distinguished: (a) epistemic uncertainty, namely a finite-sample uncertainty; (b) aleatoric uncertainty, that reflects intrinsic randomness of outcomes; and (c) uncertainty due to unobserved variables, which includes violations of identifying assumptions such as unconfoundedness or full observability. While (a) the epistemic uncertainty is relatively well studied, the latter two, (b) aleatoric uncertainty and (c) uncertainty due to unobserved variables, received way less attention.  Hence, in my dissertation, I develop novel methodological and theoretical contributions to rigorously quantify (b) and (c) for modern causal ML. The dissertation consists of three main parts: Part I (Aleatoric uncertainty), Part II (Uncertainty due to unobserved variables), and Part III (Combining both uncertainties). 

The first part (Aleatoric Uncertainty) advances causal ML beyond mean treatment effects towards a full distributional modelling. Here, I introduce two methods for flexible estimation/learning of the distribution of the potential outcomes. The first one, namely Interventional Normalizing Flows, provides a fully-parametric deep model for learning population-level distributions of potential outcomes. At the same time, the second one, namely Generative Doubly-Robust learners, extends the first one by offering a model-agnostic approach for the individualized distributions of potential outcomes. Both methods possess multiple favorable theoretical properties, for example, efficiency and double robustness, that are important for their real-world application.       

The second part (Uncertainty due to Unobserved Variables) studies a different type of uncertainty that stems from a lack of identifiability (ability to infer a treatment effect given the infinite data). Here, I also propose two methods, each in a different setting. In the first one, I discover that many state-of-the-art representation learning methods may lose their consistency due to a representation-induced confounding bias, and, as a remedy, I propose a representation-agnostic refutation framework. In the second one, I develop a partial identification framework for the counterfactual continuous outcomes, namely, Curvature Sensitivity Model. This new framework works under more realistic assumptions about structural causal models and enables an informative counterfactual inference.

Then, the third, final part (Combining Both Uncertainties) proceeds with a study of the aleatoric uncertainty of the treatment effect, which is itself only partially identifiable. Here, I introduce a novel class of model-agnostic methods, namely, Aleatoric Uncertainty learners, that aim at learning the partial identification bounds on the cumulative distribution function of the treatment effect. Again, the proposed method possess multiple favorable properties like efficiency and double robustness.  

Taken together, the contributions of this dissertation provide a coherent toolbox for uncertainty quantification in causal machine learning. These advances strengthen the reliability of causal ML in high-stakes domains such as healthcare, economics, and policy, where decisions require not only point treatment effect estimates but also the quantification of the surrounding uncertainty.

Recommended citation: 
```bibtex
@phdthesis{melnychuk2026uncertainty,
  title={Uncertainty quantification in causal machine learning},
  author={Melnychuk, Valentyn},
  year={2026},
  school={Ludwig-Maximilians-Universit\"at M\"unchen},
  type={Dissertation},
  doi={10.5282/edoc.37918},
  url={https://edoc.ub.uni-muenchen.de/37918/}
}
```
