---
title: "A Deep Dive into On-Policy TD Control: The SARSA Algorithm"
date: 2025-09-18
description: "How on-policy learning makes agents cautious by design."
summary: "Deep dive into SARSA, a foundational on-policy TD control algorithm for reinforcement learning."
tags: ["Reinforcement Learning", "Machine Learning", "SARSA", "TD Learning"]
categories: ["technical"]
showTableOfContents: true
math: true
---

{{< katex >}}

## Introduction

How does a reinforcement learning agent learn to make optimal decisions by evaluating the consequences of its own actions in real-time? This article provides a deep dive into **SARSA**, a cornerstone on-policy algorithm that elegantly answers this question. We will build our understanding from the ground up, starting with the foundational concept of Q-functions, navigating the crucial exploration-exploitation trade-off, and assembling the complete SARSA update rule.

## From State Values to Action Values: The Need for Q-Functions

### The Limitation of State-Value Functions in Model-Free Settings

In model-based reinforcement learning, the state-value function, **V(s)**, quantifies the expected future reward from a state _s_. If the environment's dynamics—the transition probabilities **P(s'|s,a)**—are known, an agent can perform a one-step lookahead to find an optimal policy. It calculates the expected value of resulting states for each action and chooses the best one.

However, in model-free scenarios, the agent lacks these transition probabilities. The state-value function becomes powerless for action selection. Knowing a state _s'_ is valuable is useless if the agent doesn't know which action leads there. $V(s)$ tells us the "goodness" of a location but provides no map for how to navigate from it.

### Introducing Action-Value Functions (Q-Functions) for Direct Control

To overcome this, we shift from evaluating states to evaluating state-action pairs. The **action-value function**, or **Q-function**, denoted as $Q(s,a)$, defines the expected return after taking action _a_ in state _s_ and following the policy thereafter.

The Q-function elegantly solves the model-free problem by bundling the action directly into the value estimate. By learning the value of each $(state, action)$ pair, the agent no longer needs a model. To make a decision, it simply compares the Q-values for all available actions in its current state. The policy becomes a simple matter of selecting the action with the highest Q-value:

$$
\pi(s) = \text{argmax}_a Q(s,a)
$$

Effectively, the Q-function caches the results of a model-based lookahead. By learning these values directly from experience, an agent can determine the best course of action without simulating outcomes.

### Q-Functions and Generalized Policy Iteration (GPI)

This learning process fits into the **Generalized Policy Iteration (GPI)** framework, which describes the interaction between policy evaluation and policy improvement:

1. **Policy Evaluation**: The agent estimates the Q-function, $Q(s,a)$, for its current policy by interacting with the environment and observing outcomes.
2. **Policy Improvement**: The agent improves its policy by making it greedy with respect to the current Q-function estimates.

By alternating between these two processes, the agent's policy converges toward optimality without needing an explicit model of the world.

---

## On-Policy Learning and the Exploration-Exploitation Dilemma

### Defining On-Policy Learning

The most intuitive way to learn is by observing the consequences of your own actions. This is the essence of **on-policy learning**. The agent improves the same policy that it uses to make decisions. The policy dictating actions (the _behavior policy_) and the policy being improved (the _target policy_) are one and the same.

Think of a chef refining a recipe by tasting the dish as they cook. They learn about the recipe (target policy) by following it directly (behavior policy). The learning process is grounded in the agent's actual experience. This contrasts with **off-policy learning**, where an agent improves a target policy by observing a different, often more exploratory, behavior policy.

### The Challenge: Balancing Exploration and Exploitation with ε-Greedy

The on-policy approach creates a critical dilemma. If an agent only ever chooses the action with the highest current Q-value (a purely greedy approach), it risks getting stuck in a suboptimal strategy. This is the classic **exploration-exploitation trade-off**:

- **Exploitation**: Using current knowledge to maximize immediate reward.
- **Exploration**: Trying other, seemingly inferior, actions to discover a potentially better long-term strategy.

A common solution is the **ε-greedy (epsilon-greedy) policy**, which balances this trade-off:

- With probability $1-ε$, the agent **exploits** by choosing the action with the highest estimated Q-value.
- With probability $ε$, the agent **explores** by selecting an action uniformly at random.

The parameter $ε$ (e.g., 0.1) controls the level of exploration. This simple rule provides a crucial guarantee: given enough time, every action in every state will eventually be tried. This continual exploration prevents Q-value estimates from stagnating and allows on-policy methods to reliably converge toward an optimal policy.

---

## The SARSA Algorithm: On-Policy TD Control in Action

### The SARSA Update: Learning from (S, A, R, S', A')

SARSA is a powerful algorithm that embodies on-policy Temporal-Difference (TD) control. Its name is a mnemonic for the tuple of data required to perform a single update: **(S, A, R, S', A')**.

This quintuple represents one full cycle of experience: from a **State** (S), an **Action** (A) is taken, leading to a **Reward** (R) and a new **State** (S'). From that new state, a new **Action** (A') is selected according to the policy.

The core of SARSA is its update rule, which adjusts $Q(S, A)$ to be closer to a more accurate estimate called the **TD Target**. The key insight of SARSA is how this target is formed:

$$
TD\ Target = R + \gamma \cdot Q(S', A')
$$

Here, $A'$ is not a hypothetical best action. It is the **actual action** that the agent's current behavior policy (e.g., ε-greedy) selected to take from state $S'$. The algorithm updates its value function based on the action it is _committed to taking next_. Because the policy used to select $A'$ is the same one being improved, the learning is "on-policy." The agent learns the value of its own policy, complete with its exploratory tendencies.

### The SARSA Algorithmic Flow

A single update step within an episode proceeds as follows:

1. From the current state $S_t$, use the policy (e.g., ε-greedy) to choose an action, $A_t$.
2. Execute $A_t$, and observe the reward $R_{t+1}$ and new state $S_{t+1}$.
3. **Crucial On-Policy Step:** In state $S_{t+1}$, use the _same_ policy to choose the _next_ action, $A_{t+1}$ (this action is not yet executed).
4. With the complete quintuple $(S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1})$, update the value $Q(S_t, A_t)$.

This loop—act, observe, select next action, update—is the heartbeat of SARSA.

### SARSA Pseudocode

```text
Initialize Q(s, a) arbitrarily for all state-action pairs
Repeat for each episode:
    Initialize state S
    Choose action A from S using policy derived from Q (e.g., ε-greedy)
    Repeat for each step in the episode:
        Take action A, observe reward R and next state S'
        Choose action A' from S' using policy derived from Q
        Update Q(S, A): Q(S, A) ← Q(S, A) + α [R + γ Q(S', A') − Q(S, A)]
        S ← S'
        A ← A'
    until S is terminal
```

---

## SARSA's Path to Optimality: The GLIE Condition

Will SARSA reliably find the best possible policy? The answer is yes, provided its policy adheres to a condition known as **GLIE**: _Greedy in the Limit of Infinite Exploration_. GLIE is a formal contract that ensures an agent explores thoroughly before committing to an optimal strategy. A GLIE policy must satisfy two conditions as learning approaches infinity:

1. **Infinite Exploration**: Every state-action pair must be visited an infinite number of times. This ensures all possibilities are continually evaluated.
2. **Greedy in the Limit**: The policy must eventually stop exploring and become purely greedy, always selecting the action with the highest estimated value.

A standard ε-greedy policy with a fixed ε satisfies the first condition but fails the second, as it never stops exploring.

The most common way to achieve GLIE is to use an ε-greedy policy where ε **decays over time**. The exploration rate starts high and is gradually reduced across episodes. This schedule ensures that all actions continue to be explored over the long run, while also ensuring the policy ultimately becomes greedy.

Because SARSA is an on-policy algorithm, guiding it with a GLIE-compliant policy (like decaying ε-greedy) guarantees that its learned action-values and policy will converge to the optimal ones, $q$ and $\pi$.

---

## Case Study: SARSA's Cautious Nature in the Cliff Walking Problem

### The Cliff Walking Environment

The Cliff Walking gridworld highlights the trade-off between risk and reward. An agent must navigate from a start state to a goal state. Between them lies a "cliff."

- Each step incurs a reward of -1.
- Stepping into the cliff incurs a reward of -100 and resets the agent to the start.

The mathematically optimal path runs along the cliff's edge. A longer, safer path exists that avoids the cliff entirely.

### Why SARSA Chooses the Safe Path

When trained with an ε-greedy policy, SARSA does not learn the mathematically optimal path. Instead, it converges to the longer, safer policy that avoids the cliff.

This seemingly suboptimal behavior reveals SARSA's core character. The reason lies in its on-policy update rule, which uses the quintuple $(S, A, R, S', A')$. The next action, $A'$, is chosen by the ε-greedy policy. For any state adjacent to the cliff, the greedy action is to move parallel to the edge. However, there is a small probability ($ε$) that the exploratory action $A'$ will be to move 'down'—directly into the cliff.

When this catastrophic event occurs, the Q-value for the preceding state-action pair is updated with a large negative reward. Over many episodes, the Q-values for all state-action pairs along the cliff's edge are penalized by the real possibility of an exploratory misstep. The algorithm correctly learns that being near the cliff is inherently low-value _because its own policy makes it dangerous_.

This behavior is a feature, not a bug. SARSA generates a realistic valuation of its policy that accounts for the risks of its own exploration. It concludes that the cumulative penalty from occasionally falling off the cliff outweighs the benefit of the shorter path, leading it to learn a cautious but effective strategy. This makes SARSA particularly useful in scenarios where exploratory mistakes are costly.

In the cliff example, SARSA avoids the risky edge because its **on-policy updates** include the consequences of exploratory actions chosen by its ε-greedy policy. Since these occasional missteps lead to falling off the cliff, the Q-values near the edge get penalized, and the agent ultimately learns the safer path.

---

## Conclusion

SARSA provides a powerful framework for on-policy TD control, learning the value of an agent's actions by using the full $(S, A, R, S', A')$ experience to guide its updates. Its defining characteristic is that it learns from the reality of its own behavior, producing a realistic valuation that accounts for the risks of its exploratory policy and often leading to safer, more cautious strategies. Understanding this on-policy approach is crucial, as it provides a sharp contrast to off-policy methods like Q-learning, which learn from hypothetical optimal actions rather than the agent's actual choices.
