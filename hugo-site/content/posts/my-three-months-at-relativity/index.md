---
title: "My Three Months at Relativity: Building AI for Legal Tech"
date: 2025-09-07
description: "Experiences, Learnings and Reflections"
summary: "Reflections on building AI for legal tech during my Applied Science internship at Relativity."
tags: ["internships", "applied science"]
categories: ["career"]
showTableOfContents: true
---

I spent the last three months as an Applied Science Intern at Relativity, working on how AI gets deployed in the legal tech domain. The experience taught me something I hadn't expected: in high-stakes fields, the technology is often the easy part.

**[Relativity](https://www.relativity.com/)** leads the e-discovery platform space, helping lawyers and legal teams turn e-discovery into easy discovery. From early-stage case preparation to production, they enable teams to move seamlessly through each phase of legal matters in one platform.

I worked in their Applied Science Team, whose role is to develop AI solutions powered by Azure and models like the GPT series and Gemini, extracting full value from these models within legal tech. It was an interesting and fun-filled journey where I understood what it takes to build AI applications for the future, how to think about AI models holistically, and how to work with customer and highly proprietary data in this age of generative AI.

## The Start

I joined the **[aiR for Review](https://www.relativity.com/data-solutions/air/review/)** team, which builds document review tools. The product helps firms process hundreds of thousands of documents to identify what matters—like the difference between reading every page in a library versus knowing exactly which three books contain what you need.

The legal teams faced a common challenge: processing millions of documents without knowing their contents upfront. Was there something critical? Something relevant? Traditional approaches required exhaustive manual review. (Like Mike Ross reading through thousands of documents overnight to find that one critical piece, or identifying red flags that might disrupt a case. Reference: IYKYK)
I worked primarily on solving this problem.

## A Different Kind of Problem Statement

My internship diverged from the traditional model where you receive a problem statement and code through it. It was completely opposite.
Since this was a new project, I worked with other smart interns, engineers, and managers from Product, UI/UX, and Software Engineering to develop solution approaches. I attended customer interviews, participated in brainstorming sessions, and helped define the problem statement. Only then did I work on solving it from an applied science perspective.

This journey taught me how to build new products in domains where stakes are high—legal tech, healthcare, finance—where clients have top-secret data, reputations depend on accuracy, and there's no room for mistakes.

## Lessons from Building GenAI in Critical Domains

### Frontier Models as Problem Solvers

Deep learning models are universal approximators, theoretically capable of solving any problem given sufficient constraints like data, compute, and scale. I'm seeing this become reality through frontier models like GPT-5 and Gemini, which can solve complex problems through proper prompt engineering or orchestrating multiple LLM calls.

The transformation in how we approach problems is striking. Since models are powerful enough, I could achieve desired results through accurate prompt engineering, efficient RAG mechanisms, or partial fine-tuning (rarely - if required). Models are becoming cheaper and more powerful—the cost per million tokens continues dropping significantly. This means we can build and deliver value lot more for less costs.

As Andrej Karpathy put it, "English is the hottest programming language." These models represent a new abstraction for solution creation, different from past approaches using mathematical models with parameters to model data and problems.

The main challenges remain: Can I trust this model? How do I measure its success ? How can I understand what it's doing under the hood? Interpretability remains fascinating and crucial.

### Problems Aren't Just Technical

I needed to understand what I was building and for whom. Through constant discussions with UX teams, PMs, and customer interactions, I witnessed how product evolution happens and what each team contributes.

Initially, the process felt slow—iteratively building with agreement from all teams. But I came to understand that building the right thing fast beats just building something fast.

During customer interactions, I learned that how I conceptualize a problem differs from how customers see it. I had to understand their perspective, then apply my knowledge to build what the market needs.

### Cross-Functional Work: Different Perspectives Matter

I spent considerable time with teams outside my background. Product managers focused on user workflows. UX designers questioned categorization schemes. Engineers pushed back on latency requirements. Initially, this felt slow—iteratively building with agreement from all teams. But I came to understand that building the right thing fast beats just building something fast.

Through customer interactions, I learned that what I considered a problem wasn't how customers saw it. I had to understand their perspective, then combine it with technical knowledge to build something valuable. The evolution of product building revealed how each team's contribution shaped the final solution.

### Developing GenAI Solutions Where Data Is Scarce and Secure

Working on a feature from scratch revealed how difficult it is to develop GenAI solutions for niche, secure domains like legal tech. The core issue: data is scarce, not easily accessible, and highly secure. No company shares sensitive lawsuit details with an intern wanting to prototype. Though I was fortunate enough to almost get into a position of doing such an experiment.

To develop these applications, I needed data for testing and labeled datasets for evaluation and benchmarking—nearly impossible to obtain directly. The solution was using existing real-world datasets or creating synthetic datasets that mimic real-world conditions. It works surprisingly well.

I created benchmarking datasets by analyzing available documents, sampling representative ones, and generating synthetic data to fill gaps in document types and risk categories. This approach overcame the fundamental constraint while maintaining contextual relevance.

## My Thoughts

Through this experience, several things became clear.
Large Language Models are becoming increasingly capable of tackling complex problems when properly enabled. The technology exists; it's about thoughtful application.  Domain-specific problems in legal, healthcare, finance, and aerospace can be addressed through dedicated testing and specialized environments. Each domain has peculiarities, but they're manageable with the right approach.

There's value in developing projects that solve problems in niche domains using powerful models—especially where AI implementation once seemed impossible.
Applied Science is an exciting field that deserves exploration in both breadth and depth. This means rapidly trying new approaches while also creating value in domains where AI might have been considered unfeasible.

The work at Relativity demonstrated that building AI solutions for critical business domains requires more than technical excellence. It demands domain understanding, cross-functional collaboration, and creative approaches to constraints like data scarcity. As frontier models evolve and become more accessible, the potential for transformative solutions in specialized fields continues expanding.

The interesting work isn't just making models better—it's making them useful where stakes are high and error tolerance is low. That's harder than it sounds, but it's where real impact happens.
