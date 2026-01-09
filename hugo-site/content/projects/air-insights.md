---
title: "aiR Insights - Legal Document Intelligence"
description: "AI-powered legal document intelligence system with LLM-as-a-Judge validation framework"
summary: "Production legal document processing system using LLM-as-a-Judge framework, achieving 87.5% accuracy with 60% time reduction."
date: 2025-06-01
tags: ["Production AI", "LegalTech", "LLM", "Enterprise"]
company: "Relativity"
position: "Applied Science Intern"
showTableOfContents: true
---

## Legal Document Intelligence at Scale

aiR Insights is a production AI system built during my internship at Relativity that processes legal documents using a two-phase LLM pipeline with automated quality validation. The system transforms manual document review into automated triage, enabling legal teams to rapidly assess risk and extract critical insights.

## Technical Architecture

### Two-Phase Processing Pipeline

**Phase 1: Extraction**
- Six AI-powered insights: document titles, summaries, structured summaries, document types, red flags, quality scores
- Tiered processing strategy: GPT-4o for high-stakes documents, GPT-4o-mini for bulk processing
- Synthetic data generation combining 200 real legal corpus samples with 400+ generated documents

**Phase 2: Validation**
- LLM-as-a-Judge framework for automated quality assessment
- Structured JSON output enforcement (100% hallucination elimination)
- MLFlow tracking across three prompt engineering iterations

## System Performance

### Quantitative Results
- **Documents Processed**: 44,420+ legal documents
- **Accuracy**: 87.5% correlation with human review
- **Time Reduction**: 60% decrease in document review time
- **Cost Optimization**: 40% reduction through tiered processing
- **Red Flag Detection**: 31.7% identification rate
- **Processing Speed**: 1,000+ documents per hour

### Data Engineering Impact
- Created 600+ document benchmark dataset
- Improved model coverage from 60% to 95% for underrepresented categories
- Built Databricks labeling system with 95% inter-rater agreement
- YAML configuration framework adopted by 3 other Applied Science projects

## Technology Stack

**Core Infrastructure**
- Azure OpenAI (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- Azure Databricks for data processing
- MLFlow for experiment tracking

**Development**
- Python for pipeline orchestration
- YAML for configuration management
- Structured JSON outputs for validation

**Evaluation**
- Custom benchmark datasets
- Human-in-the-loop validation
- Inter-rater agreement metrics

## Cross-Functional Work

Led collaboration across Product, UX, and Engineering teams through 10+ customer interviews to define system requirements. This approach ensured solutions addressed real customer needs in high-stakes legal environments where accuracy is critical.

## Professional Impact

This work reinforced my understanding that in safety-critical domains, "building the right thing fast beats just building something fast." The system successfully shipped into production handling real legal documents with liability implications, requiring rigorous validation and systematic quality assurance.
