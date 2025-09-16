---
layout: post
title: "Temporal Difference: Bootstrapping in Reinforcement Learning"
date: 2025-09-17 00:16:44+05:30
description: "Understanding differences between TD Learning and MC Learning in RL"
tags: [Reinforcement Learning]
categories: [technical]
giscus_comments: true
related_posts: false
featured: false
---
# The Core of TD Learning: Bootstrapping from a Single Step

The challenge in reinforcement learning is often one of timing: how can an agent learn effectively without waiting for the final outcome of a long sequence of actions? The answer lies in the update rule of Temporal Difference (TD) learning, specifically its most fundamental form, TD(0).

At its heart is a powerful equation for updating the value estimate of a state, $V(S_t)$. After an agent in state $S_t$ takes an action, receives a reward $R_{t+1}$, and transitions to the next state $S_{t+1}$, it adjusts its value estimate using the following rule:

$$
V(S_t) \leftarrow V(S_t) + \alpha [R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]
$$

The term $R_{t+1} + \gamma V(S_{t+1})$ is the **TD Target**. It represents a new, more informed estimate for the value of $S_t$ by combining two key pieces of information:

1. **Actual Reward ($R_{t+1}$):** A piece of factual, ground-truth experience.
2. **Estimated Future Value ($\gamma V(S_{t+1})$):** The discounted value of the *next* state, which relies on the agent's current knowledge.

This process of updating an estimate using another estimate is called **bootstrapping**. The expression within the brackets, $[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)]$, is the **TD Error** ($\delta_t$). This value is the central learning signal, quantifying the discrepancy between the new target and the old estimate. A positive error nudges $V(S_t)$ upwards, while a negative error nudges it downwards. The learning rate, $\alpha$, controls the size of this adjustment.

The profound implication of this rule is its immediacy. An agent doesn't need to wait for an episode to terminate; it can learn from each transition as it happens. This property enables **online, step-by-step learning**, making TD methods highly efficient.

This stands in stark contrast to **Monte Carlo (MC)** methods, which must wait until an entire episode is complete. MC updates are based on the full, actual return, making them unbiased but slow to learn. TD short-circuits this process, learning from incomplete episodes, but its updates are based on an estimate, which introduces a statistical trade-off we will explore next.

## The Bias-Variance Tradeoff: A Statistical Comparison

Choosing between Monte Carlo (MC) and Temporal Difference (TD) learning is a fundamental statistical trade-off. The core of this decision lies in the classic machine learning dilemma: bias versus variance.

### Monte Carlo: Unbiased with High Variance

The MC approach updates its value estimate, $V(s)$, using the full, observed return, $G_t$. Because the update target is the actual, complete outcome, the MC estimate is an **unbiased** estimator of the true value function, $V^\pi(s)$. On average, its target is perfectly correct.

However, its major drawback is **high variance**. The return $G_t$ is the sum of all future rewards and can fluctuate dramatically between episodes, as it accumulates randomness from every subsequent action and state transition. This noisy signal can make convergence slow and unstable.

### Temporal Difference: Biased with Low Variance

In contrast, the TD(0) update target is $R_{t+1} + \gamma V(S_{t+1})$. Its reliance on the current value estimate, $V(S_{t+1})$, is the source of its primary statistical property: **bias**. Early in training, $V(S_{t+1})$ is likely inaccurate, meaning the update target is systematically skewed.

The benefit of accepting this bias is a significant reduction in **variance**. The TD target's randomness is confined to a single time step—the immediate reward $R_{t+1}$ and the transition to $S_{t+1}$. The accumulated randomness of the rest of the episode is replaced by the stable, though potentially inaccurate, estimate $V(S_{t+1})$. This creates a much more consistent learning signal, which is why TD characteristically converges faster than MC.

### The Mean Squared Error (MSE) Perspective

The bias-variance tradeoff is best understood through Mean Squared Error (MSE), which can be decomposed into two components:

$$
\text{MSE} = \text{Variance} + (\text{Bias})^2
$$

* **Monte Carlo** eliminates the $\text{Bias}^2$ term but often suffers from a large Variance term.
* **Temporal Difference** introduces a non-zero $\text{Bias}^2$ term but dramatically slashes the Variance term.

In most complex problems, the instability caused by high variance is the more significant obstacle. TD's strategy of accepting some bias to gain stability is its secret weapon for efficient learning.

## Bridging the Gap: N-Step TD Learning

We've established a dilemma: the high-variance, unbiased world of MC versus the low-variance, biased approach of TD(0). N-step TD learning reveals that we don't have to choose an extreme, offering a spectrum of possibilities between these two poles.

The core idea is to look ahead a fixed number of steps, `n`, accumulate the observed rewards, and then bootstrap using the estimated value of the resulting state. This target is the **n-step return**, $G_{t}^{(n)}$:

$$
G_{t}^{(n)} = R_{t+1} + \gamma R_{t+2} + ... + \gamma^{n-1}R_{t+n} + \gamma^{n}V(S_{t+n})
$$

This formula reveals that TD(0) and Monte Carlo are endpoints on a single continuum controlled by `n`:

* When **n = 1**, the formula becomes $R_{t+1} + \gamma V(S_{t+1})$, which is the **TD(0) target**.
* When **n $\rightarrow \infty$** (i.e., reaches the end of an episode), the bootstrapped term vanishes, leaving the sum of all discounted rewards—the **Monte Carlo return**.

By adjusting `n`, we gain direct control over the bias-variance tradeoff. A **small `n`** is more biased but has low variance. A **large `n`** is less biased but has higher variance, as it incorporates a longer sequence of real reward samples. In practice, an intermediate value for `n` often outperforms both pure TD(0) and pure Monte Carlo. This concept is generalized further in advanced methods like TD($\lambda$), which elegantly combines returns across all possible `n`-step lookaheads.

## Why TD and MC Converge Differently: A Case Study

To grasp the fundamental difference between Monte Carlo and Temporal-Difference learning, we can use the classic A-B example from ***The RL Book by Sutton and Barto***. This thought experiment reveals the core assumptions each method makes about the environment and the data it learns from.

### The Scenario: A Two-State MDP

Imagine an environment with two states, A and B, and a terminal state.

* From state **A**, one action goes to **B** (reward 0), and another goes to **terminal** (reward 0).
* From state **B**, one action always goes back to **A** (reward +1).

Let's assume a policy that chooses each with 50% probability.

Now, imagine we are given a batch of eight episodes, and in every single one, the trajectory is `A -> terminal`, yielding a return of 0. The central question is: given *only this experience*, what is the value of state A?

### Monte Carlo's Answer: V(A) = 0

MC's logic is direct: it averages the complete, observed returns. Since every observed episode starting from A had a return of 0, MC calculates V(A) as the average of these returns, which is 0.

MC provides an estimate that best fits the training data. Its objective is to minimize the **mean squared error (MSE)** against the actual, observed sample returns. It makes no attempt to infer possibilities beyond the literal, observed outcomes.

### Temporal Difference's Answer: V(A) ≈ 0.75

TD operates differently. It doesn't just average returns; it seeks a value function that is self-consistent with a model of the environment. Even though the `A -> B` transition was never observed, the problem description states it is possible.

In a batch setting, TD implicitly performs a two-stage process:

1. **Model Building:** It constructs the **Maximum Likelihood Estimate (MLE)** of the underlying Markov Decision Process (MDP) from the problem's known dynamics. This model represents the most likely transition probabilities and rewards.
2. **Value Calculation:** It then computes the true value function *for that specific model*.

TD finds the value function that is correct for the assumed MDP, making it vastly more data-efficient if the environment is truly Markovian. This is why TD and MC can arrive at different answers from the same data: they are fundamentally solving two different optimization problems. Checkout the math with subtitutions to understand how we arrived at 0.75 for V(A).

---

### Why TD Converges to V(A) ≈ 0.75

We derive this step by step using the **TD(0) update rule**.

#### 1. TD(0) Update Rule

For any transition $(S_t, R_{t+1}, S_{t+1})$:

$$
V(S_t) \;\leftarrow\; V(S_t) + \alpha \Big( R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \Big)
$$

- $\alpha$ = learning rate
- $\gamma$ = discount factor
- **TD error**:

$$
\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)
$$

At convergence, the **expected TD error is zero**, so we can solve directly for the fixed-point values of $V(s)$.

---

#### 2. Dynamics of the A–B MDP

- **From state A**:
  - With probability $0.5$: go to terminal, reward $0$.
  - With probability $0.5$: go to state $B$, reward $0$.

$$
\mathbb{E}[R + \gamma V(S') \mid S=A] = 0.5 \cdot (0 + \gamma \cdot 0) + 0.5 \cdot (0 + \gamma V(B)) 
= 0.5 \gamma V(B)
$$

So at convergence:

$$
V(A) = 0.5 \gamma V(B) \tag{1}
$$

---

- **From state B**:
  - Always transitions to state $A$, reward $1$.

$$
\mathbb{E}[R + \gamma V(S') \mid S=B] = 1 + \gamma V(A)
$$

So at convergence:

$$
V(B) = 1 + \gamma V(A) \tag{2}
$$

---

#### 3. Solving the System

Substitute (2) into (1):

$$
V(A) = 0.5 \gamma (1 + \gamma V(A))
$$

$$
V(A) = 0.5\gamma + 0.5\gamma^2 V(A)
$$

Rearrange:

$$
V(A) - 0.5\gamma^2 V(A) = 0.5\gamma
$$

$$
V(A)(1 - 0.5\gamma^2) = 0.5\gamma
$$

$$
V(A) = \frac{0.5\gamma}{1 - 0.5\gamma^2} \tag{3}
$$

---

#### 4. Plugging in $\gamma = 0.9$

$$
V(A) = \frac{0.5 \times 0.9}{1 - 0.5 \times (0.9)^2}
= \frac{0.45}{1 - 0.405}
= \frac{0.45}{0.595}
\approx 0.756
$$

So:

$$
V(A) \approx 0.75, \quad V(B) = 1 + \gamma V(A) \approx 1.68
$$

---

#### 5. Key Insight

- **Monte Carlo**: Only averages observed returns. Since all observed episodes from A went straight to terminal, MC gives:

$$
V(A) = 0
$$

- **Temporal Difference**: Forces the estimates to satisfy the **Bellman equations**. This incorporates the *possibility* of $A \to B$, even if unseen, because the expected TD error must vanish.

Thus, TD’s **bootstrapping** leads to a self-consistent solution:

$$
V(A) \approx 0.75
$$

---

## Conclusion

Temporal Difference learning revolutionized reinforcement learning by introducing bootstrapping, enabling agents to learn from each step rather than waiting for a final outcome. This core distinction from Monte Carlo methods frames the critical bias-variance tradeoff, where TD accepts bias to drastically reduce variance and accelerate learning. Ultimately, understanding that these approaches are not just different algorithms but endpoints on a spectrum—from the single-step TD(0) to the full-episode MC—empowers developers to control this tradeoff and build more efficient, adaptable agents. Beyond state-value methods, **SARSA** (on-policy) and **Q-learning** (off-policy) extend TD learning to directly estimate action-value functions, making them foundational for modern reinforcement learning.
