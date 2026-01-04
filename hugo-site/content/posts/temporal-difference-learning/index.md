---
title: "Temporal Difference: Bootstrapping in Reinforcement Learning"
date: 2025-09-17
description: "Understanding differences between TD Learning and MC Learning in RL"
summary: "Understanding the TD learning update rule and bootstrapping in reinforcement learning."
tags: ["Reinforcement Learning"]
categories: ["technical"]
showTableOfContents: true
math: true
---

{{< katex >}}

The challenge in reinforcement learning is often one of timing: how can an agent learn effectively without waiting for the final outcome of a long sequence of actions? The answer lies in the update rule of Temporal Difference (TD) learning.

## The Core of TD Learning: Bootstrapping from a Single Step

At its heart is a powerful equation for updating the value estimate of a state, $V(S_t)$. After an agent in state $S_t$ takes an action, receives a reward $R_{t+1}$, and transitions to the next state $S_{t+1}$, it adjusts its value estimate using the following rule:

$$
V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]
$$

The term $R_{t+1} + \gamma V(S_{t+1})$ is the **TD Target**. It represents a new, more informed estimate for the value of $S_t$ by combining two key pieces of information:

1. **Actual Reward ($R_{t+1}$):** A piece of factual, ground-truth experience.
2. **Estimated Future Value ($\gamma V(S_{t+1})$):** The discounted value of the *next* state, which relies on the agent's current knowledge.

This process of updating an estimate using another estimate is called **bootstrapping**.

## The Bias-Variance Tradeoff

Choosing between Monte Carlo (MC) and Temporal Difference (TD) learning is a fundamental statistical trade-off.

### Monte Carlo: Unbiased with High Variance

The MC approach updates its value estimate using the full, observed return. Because the update target is the actual, complete outcome, the MC estimate is an **unbiased** estimator.

However, its major drawback is **high variance**. The return can fluctuate dramatically between episodes.

### Temporal Difference: Biased with Low Variance

In contrast, the TD(0) update target relies on the current value estimate, which introduces **bias**. The benefit is a significant reduction in **variance**, which is why TD characteristically converges faster than MC.

## Mean Squared Error Perspective

$$
\text{MSE} = \text{Variance} + (\text{Bias})^2
$$

* **Monte Carlo** eliminates the Bias² term but often suffers from large Variance.
* **Temporal Difference** introduces non-zero Bias² but dramatically slashes Variance.

In most complex problems, TD's strategy of accepting some bias to gain stability is its secret weapon for efficient learning.
