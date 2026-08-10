---
title: "Quantifying Uncertainty of the Treatment Effects"
date: 2025-05-28
venue: 'relAI blog'
link: 'https://zuseschoolrelai.de/blog/quantifying-uncertainty-of-the-treatment-effects/'
read_time: false
permalink: /posts/2025/05/quantifying-uncertainty-of-the-treatment-effects/
excerpt: "![Ladder of causation](/images/blog-au-learner.png){: style='float: left; width: 250px; margin-right: 15px; margin-bottom: 5px'} Most of causal machine learning stops at the conditional average treatment effect (CATE), but an average hides the inherent randomness in how individuals respond to a treatment — and in medicine that randomness is exactly what decides whether a therapy is safe. This post, based on our NeurIPS 2024 paper, explains why the *distribution* of the treatment effect is hard to get at: it is a counterfactual quantity (we never observe both potential outcomes for the same patient), and observational data is confounded on top of that. We introduce the AU-learner, which combines Makarov bounds with normalizing flows to estimate the range of plausible treatment-effect distributions instead of pretending a point estimate is enough — making visible the substantial minority of patients who may be harmed by a treatment that looks beneficial on average."
---

Most of causal machine learning stops at the conditional average treatment effect (CATE), but an average hides the inherent randomness in how individuals respond to a treatment — and in medicine that randomness is exactly what decides whether a therapy is safe. This post, based on our NeurIPS 2024 paper, explains why the *distribution* of the treatment effect is hard to get at: it is a counterfactual quantity (we never observe both potential outcomes for the same patient), and observational data is confounded on top of that. We introduce the AU-learner, which combines Makarov bounds with normalizing flows to estimate the range of plausible treatment-effect distributions instead of pretending a point estimate is enough — making visible the substantial minority of patients who may be harmed by a treatment that looks beneficial on average.

[Read the full post](https://zuseschoolrelai.de/blog/quantifying-uncertainty-of-the-treatment-effects/)
