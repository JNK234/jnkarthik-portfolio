---
title: "LEAR - LLM-Driven Evolution of Agent-Based Rules"
description: "Using LLMs to evolve agent behaviors in multi-agent systems through automated code generation"
summary: "Research using LLMs to evolve agent behaviors through automated code generation. Accepted at GECCO '25."
date: 2025-07-01
tags: ["Research", "AI Agents", "Evolutionary Algorithms", "NetLogo"]
externalUrl: "https://github.com/can-gurkan/LEAR"
showTableOfContents: true
---

## Evolutionary Agent-Based Modeling with LLMs

LEAR (LLM-Driven Evolution of Agent-Based Rules) is a cutting-edge research project that explores using Large Language Models within Agent-Based Modeling environments to iteratively enhance agent movement and functionality through automated code generation. This work was accepted to **GECCO '25**.

## Research Overview

### Core Innovation
This project introduces a novel methodology where evolution operates at a higher abstraction level by mutating pseudocode representations of agent behaviors, subsequently converting them into executable code through LLM-mediated steps.

### Key Contributions
- **Semantic Evolution**: Leverages LLMs to introduce semantically meaningful variations during evolution
- **Abstraction-Level Mutation**: Operates on pseudocode for more innovative solutions
- **Systematic Comparison**: Evaluates different prompting strategies for code generation
- **Multi-Agent Benchmarks**: Provides comprehensive evaluation frameworks

## Technical Approach

### Architecture Components

#### LLM-Driven Evolution
```python
# Evolution Pipeline
1. Generate initial agent behaviors
2. Evaluate performance in NetLogo environment
3. Use LLM to propose semantic mutations
4. Convert pseudocode to executable code
5. Iterate through generations
```

#### Prompting Strategies
- **Direct Code Generation**: LLM generates executable code directly
- **Pseudocode Intermediate**: Evolution on abstract representations
- **Guided Mutation**: Semantically meaningful variation operators
- **Fitness-Informed**: Performance metrics guide evolution

### Multi-Agent Domains
- Movement optimization in complex environments
- Collective behavior emergence
- Resource allocation strategies
- Swarm intelligence patterns

## Implementation Stack

**Core Technologies**
- Python with Rye management
- NetLogo for ABM
- LLM integration layer
- Evolutionary algorithms

**Evaluation Framework**
- Performance benchmarks
- Code quality metrics
- Behavioral diversity
- Convergence analysis

## Research Impact

### Academic Contributions
- **Publication**: Accepted at Genetic and Evolutionary Computation Conference (GECCO '25)
- **Novel Methodology**: First systematic exploration of LLM-driven evolution in ABM
- **Open Source**: Complete implementation and benchmarks available

### Practical Applications
- Automated agent behavior design
- Complex system optimization
- Emergent behavior discovery
- Code synthesis for simulations

## Experimental Results

### Performance Metrics
- Demonstrates superior solution quality compared to traditional GP
- Achieves faster convergence through semantic mutations
- Produces more interpretable agent behaviors
- Scales effectively to complex multi-agent scenarios

### Key Findings
- LLMs excel at introducing meaningful behavioral variations
- Pseudocode evolution enables discovery of novel strategies
- Natural language training data enhances solution creativity
- Systematic prompt engineering significantly impacts performance

## Citation

```bibtex
@inproceedings{LEAR_GURKAN,
  author = {Gurkan, Can and Jwalapuram, Narasimha Karthik and
            Wang, Kevin and Danda, Rudy and Rasmussen, Leif and
            Chen, John and Wilensky, Uri},
  title = {LEAR: LLM-Driven Evolution of Agent-Based Rules},
  year = {2025},
  booktitle = {Proceedings of GECCO '25},
  publisher = {ACM},
  doi = {10.1145/3712255.3734368}
}
```
