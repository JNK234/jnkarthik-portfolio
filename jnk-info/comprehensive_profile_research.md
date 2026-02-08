# Comprehensive Profile Research: Narasimha Karthik Jwalapuram

**Last Updated:** December 26, 2025
**Status:** Focusing on Frontier Labs (Anthropic, OpenAI, Google DeepMind, etc.)

---

## Executive Summary

Narasimha Karthik is a Research Engineer in AI Systems graduating with an MS in Artificial Intelligence from Northwestern University (December 2025). He combines production AI experience at major companies (Boeing, Relativity) with academic research publications (GECCO '25, ALife 2025) and entrepreneurial ventures (Medhastra AI, VouchAI).

**Primary Focus:** Building production AI systems at frontier labs, with emphasis on agent architectures, LLM systems, and safety-critical AI applications.

---

## Contact & Online Presence

- **Email:** narasimha@u.northwestern.edu
- **Location:** San Francisco, CA
- **Available:** December 2025
- **LinkedIn:** https://www.linkedin.com/in/narasimhakarthik
- **GitHub:** https://github.com/JNK234
- **Portfolio:** https://jnkarthik-portfolio.github.io/
- **Newsletter:** https://neuraforge.substack.com

---

## Education

### Northwestern University
**Master of Science in Artificial Intelligence** | Expected December 2025
- **Research:** CCL Lab (Computational Cognitive Learning Lab)
- **Focus:** Genetic programming with LLMs, agent-based modeling
- **Publications:** 2 peer-reviewed conference papers (GECCO '25, ALife 2025)

### PES University, Bangalore
**Bachelor of Technology in Electronics and Communication Engineering**

---

## Professional Experience

### 1. Relativity (Applied Science Intern)
**Duration:** June 2025 - August 2025
**Location:** San Francisco Bay Area

**Project: aiR Insights - Legal Document Intelligence**

Built a production AI system for legal document review processing 44,420 documents with 87.5% accuracy.

**Technical Stack:**
- Azure OpenAI (GPT-4o, GPT-4o-mini, GPT-3.5-turbo)
- Azure Databricks, MLFlow
- YAML configuration system
- Two-phase processing pipeline (extraction + validation)

**Key Innovations:**
- LLM-as-a-Judge framework for automated quality assessment
- Tiered processing strategy (GPT-4o for high-stakes, mini for bulk)
- Structured JSON output enforcement eliminating hallucinations
- Synthetic data generation using BigThorium universe

**Quantifiable Impact:**
- 60% reduction in document review time
- 31.7% of documents flagged with actionable risks
- 40% cost reduction through tiered processing
- Processes 1000+ documents per hour
- 87.5% correlation with human review

**Leadership:**
- Cross-functional work with Product, UX, Engineering, customer teams
- Conducted customer interviews and requirements gathering
- Presented findings to senior leadership

---

### 2. Boeing (Data Scientist)
**Duration:** 2022-2023

**Project: Technical Publications Automation**

**The Problem:**
- 1000s of Aerospace Maintenance Manuals (AMMs), each with 10,000+ pages
- Engineering changes via Service Bulletins (SBs)
- Manual update process: 90 days turnaround time
- Bottleneck for aircraft maintenance updates

**Technical Solution:**

1. **Custom PDF Parser:**
   - Built from scratch (standard parsers failed)
   - Converted PDFs → Markdown
   - Regex patterns for section extraction
   - Handled technical content, tables, diagrams

2. **Model Training:**
   - Full fine-tuning of GPT-2 and Mistral-7B
   - LoRA adapters for domain vocabulary
   - Instruction-tuning format dataset
   - Processed 2000+ SB documents

3. **RAG System:**
   - ChromaDB vector store
   - LangChain agent for context retrieval
   - Dynamic context without retraining
   - In-house processing (Boeing compliance)

**Impact:**
- 80% reduction in manual effort (90 days → ~18 days)
- $200k funding secured for team expansion
- Team grew from 1 → 6 engineers
- 1st place in Boeing LLM documentation hackathon
- 3rd place globally in all categories

**Other Work:**
- Cost prediction models for airplane parts
- Led NLP-LLM community of practice
- Led ML Engineer hiring process

---

### 3. Invento Robotics (iOS Developer - Internship)

**Project: Invento Fleet iOS App**

**Built:**
- iOS app with 10+ core features for robot fleet management
- Real-time video calling using TwilioVideo
- Socket-based communication system
- Human fall detection using YOLOv5

**Technologies:** Swift, iOS, WebRTC, Computer Vision (YOLOv5), Socket programming

**Impact:** 90% reduction in fleet web portal dependence

---

## Research & Publications

### 1. LEAR (GECCO '25)
**Title:** "LEAR: LLM-Driven Evolution of Agent-Based Rules"
**Venue:** Genetic and Evolutionary Computation Conference 2025
**Authors:** Can Gurkan, Narasimha Karthik Jwalapuram, Kevin Wang, Rudy Danda, Leif Rasmussen, John Chen, Uri Wilensky
**DOI:** https://doi.org/10.1145/3712255.3734368

**Contribution:** Novel methodology combining LLMs with evolutionary computation for agent behavior evolution in multi-agent systems.

**Key Features:**
- Semantic evolution using LLMs for meaningful variations
- Pseudocode-level mutation for innovative solutions
- Multi-agent benchmark evaluation frameworks
- First systematic exploration of LLM-driven evolution in ABM

**Repository:** https://github.com/can-gurkan/LEAR

---

### 2. QD-LEAR (ALife 2025)
**Title:** "QD-LEAR: Exploring Quality-Diversity Tradeoffs in LLM-Evolved Agent Rule Representations"
**Venue:** Conference on Artificial Life 2025, Kyoto, Japan
**Authors:** Narasimha Karthik Jwalapuram, Can Gurkan, Kevin Wang, Rudy Danda, Leif Rasmussen, John Chen, Uri Wilensky

**Contribution:** Research exploring quality-diversity tradeoffs in LLM-evolved agent rule representations.

---

### 3. CCL Lab Research (Northwestern)
**Project:** LEAR Research Project

**Investigated:** LLM integration with genetic algorithms for NetLogo agent behavior evolution

**Developed:**
- Framework combining Claude and Groq APIs for code generation
- Verification system for syntactically correct NetLogo code
- Performance tracking and logging systems

---

## Startup & Entrepreneurial Experience

### 1. VouchAI (Latest Project)
**Description:** First agent-to-agent insurance protocol combining Locus payments, Stripe financial rails, and Anthropic's Claude as autonomous arbiter

**Architecture:**
- Three-agent system (Hiring, Worker, Arbitrator)
- AI-powered dispute resolution using Claude
- USDC staking and collateral system
- Real-time reasoning streams
- Reputation-based trust system

**Technologies:** TypeScript, Claude Agent SDK, Locus MCP, USDC payments
**Innovation:** Smart contracts + AI judgment for trustworthy agent commerce
**GitHub:** https://github.com/JNK234/VouchAI
**Stars:** 1

---

### 2. Medhastra AI (Co-founder)

**Product Vision:** Medical education platform using AI-powered simulations for medical students and physicians

**Focus Areas:**
- Diagnostic gap detection
- Confounder analysis
- Treatment planning

**Technical Architecture (v2):**
- LangGraph-based orchestration
- Multi-agent workflow with human-in-the-loop
- Components: Medical history collection, review of systems, physical examination, differential diagnosis

**Technologies:** Python, FastAPI, LangChain, LangGraph, SQLAlchemy

**User Insights:**
- Medical students: Need premade cases, better UI, faster responses
- Physicians: Want risk/benefit analysis, clinical reasoning visualization, EMR integration

---

## Key GitHub Projects

### 1. Agentic-Blogging-Assistant
**Latest work** - Agentic system for blog content creation and management
**GitHub:** https://github.com/JNK234/Agentic-Blogging-Assistant

---

### 2. mcp-multiverse ⭐ (Starred)
**Description:** Universal MCP server sync manager for Claude Code, Gemini CLI, Cline, and Roo Code

**Features:**
- Syncs MCP servers across multiple AI platforms
- Backs up configurations before changes
- No external dependencies (Python standard library only)

**Technologies:** Python, Bash, JSON configuration
**Last Updated:** December 18, 2025

---

### 3. AdVocate-Agentic-Ad-Generator
**Description:** Agentic Advertisement Generator using Claude AI, LangGraph, and Stable Diffusion

**Architecture:**
- Three-agent system (Research, Marketing, Ad Generator)
- Automated market research using Claude AI
- LangGraph workflow orchestration
- Multi-modal content generation (text + images)

**Technologies:** Python, Claude AI, LangGraph, Stable Diffusion, Streamlit
**Last Updated:** March 12, 2025

---

### 4. Second-OpinAIon
**Description:** Medical Diagnosis with Causal Inference

**Features:**
- Causal graph analysis and visualization
- Counterfactual reasoning for diagnostic confidence
- Treatment intelligence with categorization
- Multi-stage workflow from symptom to treatment
- Automated PDF report generation

**Use Cases:** Clinical decision support, medical education, documentation
**Safety:** Designed as decision support tool requiring medical expertise
**Last Updated:** March 12, 2025

---

### 5. FaceSwap-Diffusion-Model
**Description:** DeepFake face swap using diffusion models with identity preservation

**Technical Details:**
- CelebA/CelebA-HQ dataset usage
- DDPM (Denoising Diffusion Probabilistic Model)
- Identity preservation using FaceNet/ArcFace
- Multiple evaluation metrics (FID, SSIM, LPIPS)

**Technologies:** Python, Diffusion models, Face recognition, Computer vision
**Last Updated:** March 20, 2025

---

### 6. Reinforcement-Learning-Algorithms
**Description:** Comprehensive implementation and experiments with all RL algorithms

**Purpose:** Reinforcement learning research and education
**Scope:** All major RL algorithms implemented
**Last Updated:** September 21, 2025

---

### 7. Self-evolving-agent
**Description:** Framework for Sequential Prompt Iteration and Automatic Tool Creation

**Purpose:** Autonomous agent development
**Stars:** 1 (has been forked)
**Last Updated:** November 4, 2025

---

### 8. Netlogo-LLM-Extension
**Description:** Scala extension for NetLogo with LLM integration

**Collaboration:** Research project for LEAR paper
**Technologies:** Scala, NetLogo, LLM integration

---

## Technical Writing & Community

### NeuraForge Newsletter
**Started:** August 2023
**Platform:** https://neuraforge.substack.com
**Focus:** Generative AI and Machine Learning trends

**Content Areas:**
- Large Language Models (architecture, training, deployment)
- RAG Systems (practical implementations)
- AI Engineering (production best practices)
- Research Analysis (latest papers and breakthroughs)
- Tool Reviews (hands-on evaluation)

**Popular Articles:**
- "Building Production RAG Systems: A Practitioner's Guide"
- "The Real Cost of Fine-tuning LLMs"
- "From GPT to Production: Lessons from the Trenches"

**Audience:** ML Engineers (40%), Data Scientists (30%), Technical Leaders (20%), Researchers (10%)

---

### Technical Blog Series

**Reinforcement Learning Series (2025):**
1. "The Deadly Triad in Reinforcement Learning: Why Agents Fail and How DQN Fixed It"
2. "A Deep Dive into Q-Learning: The Off-Policy TD Control Algorithm"
3. "A Deep Dive into On-Policy TD Control: The SARSA Algorithm"
4. "Temporal Difference: Bootstrapping in RL"
5. "Monte Carlo Learning in RL"

**Technical Implementation Guides:**
- "Implementing GPT-style Attention with Pytorch"
- "The Ultimate Guide to Preparing Text Data for Language Modeling"
- "PyTorch in Practice: Essential Building Blocks"
- "Beyond Supervised Learning: Reinforcement Learning"

---

## Behavioral Stories (STAR Format)

### Story 1: Working with Difficult Team Members
**Situation:** At Boeing, needed data from a colleague who was unresponsive for 2 weeks
**Task:** Critical data access blocking ML model training
**Action:**
- Continued pipeline development while waiting
- Sent reminder email
- Visited his office in person
- Learned he was waiting for supervisor approval
- Asked for approval process email to share with manager
**Result:** Got temporary resolution, data arrived, integrated without further delay
**Learning:** Proactive communication and understanding others' perspectives

---

### Story 2: Leadership (Hackathon Success)
**Situation:** Boeing company-wide hackathon announced
**Task:** Saw alignment with existing LLM project for aircraft manuals
**Action:**
- Took initiative to submit application
- Assembled team despite busy schedules
- Coordinated brainstorming sessions
- Secured compute resources
- Laid out clear 24-hour plan
- Ensured everyone understood their role
**Result:** 1st place in LLM documentation track, 3rd place globally
**Learning:** Initiative + connecting right people = outstanding success

---

## Technical Skills & Expertise

### Core AI/ML
- **LLM Engineering:** Fine-tuning (GPT-2, Mistral, LLaMA), RAG systems, prompt engineering, LLM-as-a-Judge
- **Generative AI:** Multi-modal systems, document generation, structured outputs
- **NLP:** Text extraction, parsing, semantic understanding, domain adaptation
- **Reinforcement Learning:** All major RL algorithms, TD learning, Monte Carlo methods
- **Computer Vision:** Face swapping, diffusion models, object detection (YOLOv5)
- **Agent Systems:** Multi-agent architectures, autonomous agents, agent-to-agent protocols

### MLOps & Deployment
- **Cloud Platforms:** Azure OpenAI, Azure Databricks, MLFlow, GCP
- **Model Deployment:** End-to-end pipelines, production monitoring
- **Data Engineering:** Custom parsers, PDF extraction, vector databases

### Programming & Frameworks
- **Languages:** Python, TypeScript, Swift, Scala, SQL
- **Frameworks:** PyTorch, Transformers, LangChain/LangGraph, FastAPI
- **Data Tools:** ChromaDB, vector databases
- **Web:** Streamlit, Flask

### Specialized
- **MCP (Model Context Protocol):** Tooling and synchronization
- **Claude AI Integration:** Heavily integrated across projects
- **Smart Contracts:** USDC payments, agent economies

---

## Target Companies & Roles

### Primary Focus: Frontier Labs

**Tier 1 Targets:**
- **Anthropic** - AI Safety & Research Roles
- **OpenAI** - Research Engineer
- **Google DeepMind** - AI Research

**Tier 2 Targets:**
- Jane Street - Algorithm Developer/Quant Researcher
- HRT AI Labs - Algorithm Developer/Quant Researcher
- Grok-X.ai - AI positions
- The Voleon Group - Quantitative research
- Akuna Capital - Quantitative positions

### Role Aspirations
**Primary Focus:**
- AI Research Engineer
- Applied Scientist
- Machine Learning Engineer
- Quantitative Researcher

**Career Trajectory:**
1. **Current:** Applied Science Intern → Full-time AI Engineer
2. **Near-term (2-3 years):** Senior AI Engineer / Tech Lead
3. **Mid-term (5 years):** AI Research Lead / Principal Engineer
4. **Long-term:** Technical Director / AI Research Director

---

## Unique Value Proposition

### What Makes Him Different:

1. **Safety-Critical AI Experience**
   - Aerospace (Boeing) - errors have catastrophic consequences
   - Legaltech (Relativity) - accuracy affects legal outcomes
   - Healthcare (Medhastra) - mistakes impact patient care

2. **Research + Production Bridge**
   - Published in top conferences (GECCO, ALife)
   - Production deployment at major companies
   - Can read papers and implement production systems

3. **Custom Solution Builder**
   - Built custom PDF parser when standard tools failed
   - Created domain-specific fine-tuning pipelines
   - Designed RAG systems from scratch

4. **Measurable Impact**
   - Every major project has quantifiable results
   - 80%, 90%, 60% reductions in effort/time
   - $200k funding secured
   - Multiple competition wins

5. **Cross-Domain Adaptability**
   - Successfully operated in aerospace, legaltech, healthcare, finance
   - Rapid learning and application in new domains

6. **Agent Systems Expertise**
   - Multiple multi-agent architectures
   - Agent-to-agent protocols (VouchAI)
   - LangGraph orchestration patterns
   - Autonomous agent frameworks

---

## Key Achievements Summary

### Technical Impact
- **80% reduction** in Boeing manual effort (90 days → 18 days)
- **60% reduction** in Relativity document review time
- **87.5% accuracy** in legal document classification
- **40% cost reduction** through tiered LLM processing

### Business Impact
- **$200k funding** secured for Boeing team expansion
- Team growth from **1 → 6 engineers**
- **1000+ documents/hour** processing capacity

### Recognition
- **1st place** - Boeing LLM documentation hackathon
- **3rd place** - Boeing hackathon (all categories globally)
- **2 peer-reviewed publications** (GECCO '25, ALife 2025)

### Community
- Active technical newsletter (NeuraForge)
- Open-source contributor (75+ GitHub repos)
- Starred repository (mcp-multiverse)

---

## Strengths

### Technical
- LLM fine-tuning and deployment
- RAG system design and implementation
- Multi-agent system architecture
- Custom data extraction and parsing
- End-to-end ML pipeline development
- Production deployment (Azure, MLFlow)
- Structured output generation (eliminating hallucinations)

### Methodological
- First principles problem-solving
- Iterative prototyping and validation
- Data-centric approach to ML
- User-centric product development
- Pragmatic vs. idealistic trade-offs

### Leadership
- Initiative-taking (hackathon example)
- Cross-functional collaboration
- Stakeholder management
- Team formation and coordination
- Technical communication to non-technical audiences

### Personal
- Learning agility (rapid domain switching)
- Proactive communication style
- Persistence through challenges
- User empathy and customer focus
- Entrepreneurial mindset

---

## Areas for Growth

### Technical
- **Large System Architecture:** More component experience than large-scale
- **Production Monitoring:** Limited MLOps monitoring at scale mention
- **Distributed Systems:** Not heavily emphasized

### Career
- **Team Leadership:** Led 6-person team, not larger organizations
- **Strategic Vision:** More operational than strategic experience
- **Industry Depth:** Fast domain switching may limit deep expertise

### Research
- **Top-tier Venues:** GECCO/ALife are good, but could aim for NeurIPS/ICML/ICLR
- **Solo Publications:** Most work is collaborative

---

## Assessment for Frontier Labs

### For Anthropic
**Strengths:**
- Direct Claude AI experience across multiple projects
- Safety-critical AI experience (Boeing, Relativity)
- Agent systems expertise (VouchAI, multi-agent architectures)
- Research publications in AI conferences

**Gaps:**
- Limited AI safety-specific research
- More focus on application vs. novel safety algorithms

**Fit:** **VERY HIGH** - Especially for applied safety roles, agent systems, production deployment

---

### For OpenAI
**Strengths:**
- Production LLM experience (fine-tuning, RAG)
- Multi-modal systems (AdVocate)
- Agent frameworks and orchestration
- Measurable impact in production

**Gaps:**
- Limited work on alignment specifically
- More engineering than research focus

**Fit:** **HIGH** - For Applied Research Engineer roles, particularly in agent systems

---

### For Google DeepMind
**Strengths:**
- Reinforcement learning expertise (comprehensive implementations)
- Research publications
- Multi-agent systems experience
- Technical writing and communication

**Gaps:**
- Limited RL-specific publications
- More application than novel algorithms

**Fit:** **MEDIUM-HIGH** - For applied RL/agent systems roles

---

## Recommendations

### Immediate Actions
1. **AI Safety Focus:** Emphasize safety-critical experience (Boeing, Relativity)
2. **Agent Systems:** Lead with VouchAI, multi-agent work
3. **Research Publication:** Consider targeting NeurIPS/ICML/ICLR
4. **Claude Expertise:** Highlight deep Claude AI integration work
5. **System Design:** Deepen knowledge of large-scale ML system architecture

### Career Positioning
- **Sweet Spot:** Applied AI Research Engineer at frontier labs
- **Differentiation:** Safety-critical AI + agent systems + Claude expertise
- **Narrative:** "I build production AI agent systems where safety and accuracy matter"

### Interview Strategy
- Lead with **VouchAI** (agent-to-agent protocols, Claude integration)
- Follow with **Boeing TechPubs** (80% impact, $200k funding, safety-critical)
- Highlight **Relativity aiR Insights** (60% efficiency, 87.5% accuracy, LLM-as-a-Judge)
- Emphasize **Research Publications** (GECCO, ALife)
- Demonstrate **Agent Systems Expertise** (multi-agent architectures)
- Showcase **Claude AI Integration** (across multiple projects)

### Frontier Labs Pitch
> "I'm a Research Engineer who builds production AI systems where safety matters. At Boeing, I deployed LLMs in safety-critical aerospace environments, achieving 80% automation and securing $200k funding. At Relativity, I built an LLM-as-a-Judge system for legal documents with 87.5% accuracy. My research on LLM-evolved agents has been published at GECCO and ALife. I'm now building agent-to-agent protocols (VouchAI) using Claude for trustworthy AI commerce. I combine research depth with production experience, specializing in agent systems and safety-critical applications."

---

## Summary

Narasimha Karthik is a **production-focused AI Research Engineer** with rare experience building agent systems where accuracy and safety are critical. He's delivered measurable business impact across multiple high-stakes domains (aerospace, legal, healthcare) and published novel research combining LLMs with evolutionary computation.

**His Best Fit:** Applied AI Research Engineer at frontier labs (Anthropic, OpenAI, DeepMind), especially for roles involving:
- Agent systems and multi-agent architectures
- LLM safety and reliability
- Production deployment of AI systems
- Claude AI integration and applications

**His Edge:** He doesn't just research agent systems - he builds, deploys, and scales them. He understands both the research frontier and production constraints, with a focus on safety-critical applications.

**Career Trajectory:** Well-positioned for Applied Research Engineer → AI Research Lead → Technical Director path at frontier labs focused on agentic AI, safety, and production systems.
