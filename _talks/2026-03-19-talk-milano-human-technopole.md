---
title: "Causal ML for treatment effect estimation"
collection: talks
type: "Tutorial"
venue: "<a href='https://humantechnopole.it/en/research-centres/computational-biology/'>Internal Seminar @ Computational Biology Research Centre</a>"
date: 2026-03-19
location: "Human Technopole, Milan, Italy"
slides:
---

**Abstract**: In this tutorial, I introduce causal machine learning as a practical toolkit for estimating treatment effects and counterfactuals from observational data. Here, I formalize the potential-outcomes setup and explain why individual treatment effects are not directly observable, which motivates causal identification. I then walk through the key assumptions — consistency, overlap/positivity, and exchangeability — and show how they connect to common causal frameworks (potential outcomes, SCMs, and causal graphs). Building on that foundation, I cover the main estimands (ATE and heterogeneous effects such as CATE) and compare widely used CATE estimators, from plug-in learners (S-/T-learners) to orthogonal and doubly robust approaches based on pseudo-outcomes and residualization (e.g., IPW/RA/DR and R-learning). I conclude the talk with an overview of state-of-the-art works in causal ML and a discussion of open practical challenges such as uncertainty quantification, model selection under limited data, and hidden confounding.