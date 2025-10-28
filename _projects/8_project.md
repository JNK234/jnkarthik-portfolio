---
layout: page
title: NLP Interpretability - Mechanistic Analysis of LLMs
description: Research exploring how large language models process financial statements for earnings prediction through mechanistic interpretability techniques
img: assets/img/8.jpg
importance: 2
category: research
---

## 🔬 Mechanistic Interpretability in Financial Prediction

A comprehensive research project investigating how large language models understand and predict earnings direction changes from financial statements. This work develops techniques to extract, analyze, and manipulate model attention patterns to improve prediction accuracy and transparency in financial forecasting applications.

## Research Overview

### Core Innovation
This project establishes a multi-phase mechanistic interpretability framework for understanding LLM decision-making in financial prediction, focusing on 3-class classification (earnings increase, stay same, or decrease) using the Qwen 7B model on Compustat financial data.

### Key Contributions
- **Attention Analysis Pipeline**: Word-level attention aggregation across all 36 transformer layers
- **Causal Attribution Framework**: Integrated Gradients implementation for gradient-based feature importance
- **Model Steering Techniques**: Intervention methods for controlled behavior manipulation
- **Comprehensive Evaluation**: F1 scores, confusion matrices, and error analysis for interpretability validation

## Technical Approach

### Phase 3: Attention Weight Extraction (Completed)
```python
# Current baseline implementation
- Word-level attention aggregation from inference pipeline
- Token-level analysis of model reasoning
- F1 Score: 0.606 on 1,426 predictions
- Foundation for multi-phase mechanistic analysis
```

### Research Pipeline

#### Phase 4-6 Roadmap (In Progress)
- **Full Attention Matrix Analysis**: Token-level extraction for understanding fine-grained model behavior
- **Attention Rollout**: Multi-layer information flow tracking across 36-layer architecture
- **Integrated Gradients**: Validation of causal importance for model components

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <b>Data Processing</b>
        <ul>
            <li>5,000 company observations (Compustat)</li>
            <li>Standardized financial features</li>
            <li>Chain-of-thought prompting</li>
            <li>Structured LLM outputs</li>
        </ul>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <b>Analysis Techniques</b>
        <ul>
            <li>Attention pattern extraction</li>
            <li>Activation analysis (FFN)</li>
            <li>Causal interventions</li>
            <li>Model steering vectors</li>
        </ul>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <b>Evaluation Framework</b>
        <ul>
            <li>F1 scores (macro-averaged)</li>
            <li>Confusion matrices</li>
            <li>Error analysis</li>
            <li>Attention visualizations</li>
        </ul>
    </div>
</div>

## Technical Implementation

### Infrastructure

#### Model Architecture
- **Base Model**: Qwen 7B LLM for financial reasoning
- **Processing**: 36-layer transformer with attention extraction
- **Deployment**: H100 GPU cluster via SLURM batch jobs
- **Framework**: PyTorch 2.0+ with Hugging Face Transformers

#### Interpretability Methods

**Attention Mechanisms**
- Multi-head attention weight extraction across all layers
- Word-level aggregation for semantic importance
- Temporal attention flow analysis
- Cross-sectional importance heatmaps

**Gradient-Based Attribution**
- Integrated Gradients for causal feature importance
- Gradient accumulation across prediction paths
- Attribution visualization and analysis
- Validation against attention patterns

**Activation Analysis**
- Feed-forward network neuron activation patterns
- Financial concept identification in hidden states
- Causal intervention framework
- Steering vector computation

## Key Findings

### Phase 3 Baseline Results
- **Performance**: F1 score of 0.606 on validation set (1,426 predictions)
- **Infrastructure**: Established foundational pipeline for attention extraction
- **Framework**: Token manipulation and evaluation systems operational
- **Visualization**: Attention heatmaps and temporal flow tools developed

### Research Insights
- Word-level attention reveals model focus on key financial metrics
- Multi-layer analysis exposes hierarchical information processing
- Attention patterns correlate with prediction confidence
- Foundation established for deeper causal analysis in phases 4-6

## Technology Stack

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <b>Core ML</b>
        <ul>
            <li>PyTorch 2.0+</li>
            <li>Transformers 4.30+</li>
            <li>Qwen 7B LLM</li>
            <li>Captum (attribution)</li>
        </ul>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <b>Data & Analysis</b>
        <ul>
            <li>NumPy</li>
            <li>Pandas</li>
            <li>Scikit-learn</li>
            <li>SciPy</li>
        </ul>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <b>Visualization</b>
        <ul>
            <li>Matplotlib</li>
            <li>Seaborn</li>
            <li>Plotly</li>
            <li>Custom heatmaps</li>
        </ul>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <b>Infrastructure</b>
        <ul>
            <li>SLURM scheduling</li>
            <li>H100 GPU cluster</li>
            <li>CUDA</li>
            <li>Python 3.10+</li>
        </ul>
    </div>
</div>

## Research Applications

### Financial Forecasting
- Improved transparency in earnings prediction models
- Identification of key financial indicators for model decisions
- Enhanced interpretability for regulatory compliance
- Explainable AI for financial institutions

### Mechanistic Interpretability
- Novel techniques for LLM attention analysis
- Causal intervention frameworks for financial domain
- Gradient-based attribution in specialized contexts
- Multi-phase analysis methodology

### Future Directions
- Real-time interpretability dashboards
- Extended analysis to other financial prediction tasks
- Comparison across multiple LLM architectures
- Integration with production financial systems

## Academic Context

This research contributes to the growing field of mechanistic interpretability, specifically addressing the challenge of understanding LLM behavior in high-stakes financial prediction scenarios where transparency and explainability are critical.

### Research Impact
- Establishes baseline for financial LLM interpretability
- Develops comprehensive analysis framework
- Creates reusable infrastructure for future research
- Bridges gap between NLP and financial AI

## Project Status

**Current Phase**: Phase 3 completed, Phase 4-6 in progress
**Timeline**: Ongoing research project
**Category**: Independent Study (Fall 2025)
