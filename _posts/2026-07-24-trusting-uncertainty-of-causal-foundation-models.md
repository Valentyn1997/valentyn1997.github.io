---
title: "Can We Trust the Uncertainty of Causal Foundation Models?"
date: 2026-07-24
authors: '<b>V. Melnychuk</b>'
venue: 'relAI blog'
link: 'https://zuseschoolrelai.de/blog/trusting-uncertainty-causal-foundation-models/'
read_time: false
permalink: /posts/2026/07/trusting-uncertainty-of-causal-foundation-models/
excerpt: "![Causal foundation models](/images/blog-causal-pfn.png){: style='float: left; width: 250px; margin-right: 15px; margin-bottom: 5px'} Causal foundation models promise fast, flexible treatment-effect estimation, but their uncertainty can be misleading and even carry a confounding bias. This post looks at prior-data fitted networks (PFNs) — foundation models trained on synthetic datasets to perform amortized Bayesian inference — and at how the priors they were trained on leak into the posteriors they report. The result is a *prior-induced confounding bias*: implicit assumptions baked into the training distribution make the model understate the confounding actually present in real observational data, so its credible intervals are narrower and more confident than they should be. I then discuss a one-step posterior correction, a calibration step that makes PFN-based uncertainty behave much more like the uncertainty of classical frequentist causal estimators, restoring trustworthiness in high-stakes settings such as medicine."
---

Causal foundation models promise fast, flexible treatment-effect estimation, but their uncertainty can be misleading and even carry a confounding bias. This post looks at prior-data fitted networks (PFNs) — foundation models trained on synthetic datasets to perform amortized Bayesian inference — and at how the priors they were trained on leak into the posteriors they report. The result is a *prior-induced confounding bias*: implicit assumptions baked into the training distribution make the model understate the confounding actually present in real observational data, so its credible intervals are narrower and more confident than they should be. I then discuss a one-step posterior correction, a calibration step that makes PFN-based uncertainty behave much more like the uncertainty of classical frequentist causal estimators, restoring trustworthiness in high-stakes settings such as medicine.

[Read the full post](https://zuseschoolrelai.de/blog/trusting-uncertainty-causal-foundation-models/)
