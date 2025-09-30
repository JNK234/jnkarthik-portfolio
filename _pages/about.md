---
layout: about
title: about
permalink: /
subtitle: >
  <p>Research Engineer, AI Systems</p>
  <p>MS in Artificial Intelligence • Northwestern University</p>

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Chicago, IL</p>
    <p>Available Dec 2025</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

I build agents and train LLMs for production systems. Currently at **Relativity**, I led cross-functional teams to automate legal document processing for 46K+ documents, achieving 87.5% accuracy through systematic prompt engineering and tiered LLM architectures.

At **CCL Lab (Northwestern)**, I'm developing genetic programming frameworks that evolve code generation capabilities using state-of-the-art LLMs (Grok, Claude, DeepSeek) with LangGraph orchestration for multi-agent verification systems.

Previously at **Boeing**, I secured $200k funding by building RAG systems that reduced Aircraft Maintenance Manual authoring effort by 80%. Fine-tuned GPT-2 and Llama models on 2,000+ technical documents using PEFT techniques on 4x A100 GPUs.

## Technical Approach

**Legal Document Intelligence** (Relativity)
Built insights extraction pipeline processing contracts, depositions, and discovery documents. Eliminated hallucinations through structured outputs and LLM-as-Judge validation. Created 600+ document benchmark combining real corpus with synthetic generation, improving coverage for rare categories from 0.5% to 10%.

**Autonomous Code Evolution** (CCL Lab)
Architecting hierarchical agent systems where LLMs generate, test, and evolve agent-based models through genetic programming. Implementing verification layers that evaluate correctness and performance of LLM-generated code against NetLogo benchmarks.

**Domain-Specific LLM Fine-tuning** (Boeing)
Tackled the challenge of adapting general LLMs to aerospace technical writing. Built custom PDF-to-Markdown parser for 2,000+ AMM documents when standard parsers failed. Multi-stage instruction fine-tuning using alpaca format achieved 80% generation accuracy for technical authoring.

## Stack
Python • PyTorch • LangChain/LangGraph • ChromaDB • FastAPI • Transformers • PEFT/LoRA

Recent work: [Agentic Blogging Assistant](https://github.com/JNK234/Agentic-Blogging-Assistant) (HyDE RAG with multi-LLM orchestration)

Connect: [LinkedIn](https://www.linkedin.com/in/narasimhakarthik/) • [Newsletter](https://neuraforge.substack.com)
