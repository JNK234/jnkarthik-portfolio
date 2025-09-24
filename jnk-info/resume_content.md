Name: Narasimha Karthik J

Linkedin: https://www.linkedin.com/in/narasimhakarthik/
Newsletter: https://neuraforge.substack.com

## Education

**Northwestern University**
Master of Science in Artificial Intelligence
*Expected Graduation: Dec 2025*

**PES University**
BTech in Electronics and Communication Engineering
*Graduated: Sept 2022*

## Skills

**Languages**: Python, SQL, C, Pandas, Numpy, Netlogo
**Frameworks**: PyTorch, Transformers, Sklearn, XgBoost, LangChain, FastAPI, ChromaDB, Elasticsearch, LlamaIndex
Research Interests: LLM training, Reinforcement Learning, NLP, Causal Inference, Mechanistic Interpretibility, Agentic AI

## Experience

### Relativity

Applied Science Intern | June 2025 - Aug 2025
*Chicago, Illinois*

**1. Led cross-functional initiative with Product, UX, and Engineering** through 10+ customer interviews to define 6 AI-powered insights (title, summary, structured summary, doc type, red flags, quality score), transforming manual document review into automated triage with 60% time reduction.

**2. Built insights extraction pipeline via systematic prompt engineering** (3 iterations, MLFlow tracking) with LLM-as-Judge validation, eliminating 100% hallucinations through structured outputs, and processing 46,864 legal documents.

**3. Created 600+ document benchmark dataset** combining real legal corpus (200 samples) with synthetic generation (400+ documents), improving model coverage from 60% to 95% for underrepresented categories (Governance: 0.5% → 10%).

 **4. Optimized prompts using benchmark dataset feedback loops** , achieving 31.7% red flag detection rate, 95% classification accuracy, and 40% cost reduction through tiered GPT-4o/mini processing strategy.

**5. Implemented scalable Databricks labeling system** with 95% inter-rater agreement, delivering reusable YAML configuration framework and evaluation rubrics adopted by 3 subsequent Applied Science projects.

### CCL Lab - Northwestern University

**Research Assistant** | *Sept 2024 - Present* | *Evanston, Illinois*

- Developing frameworks to perform code generation and evolve its capabilities with Genetic programming with LLMs like Grok, Claude and DeepSeek models using Langchain and LangGraph libraries
- Built verification and performance tracking systems to evaluate LLM-generated code for agent-based modeling

### The Boeing Company

**Data Scientist** | *July 2022 - Aug 2024* | *Bengaluru, India*

- Worked with a team of 2 to develop dynamic cost prediction models of airplane parts with 2M+ rows of raw dataset at Teardown Analytics Lab
- Created automated training and evaluation of regression models on tabular dataset, reducing total modeling experimentation time by 70%
- Implemented threading and multiprocessing for hyperparameter tuning, achieving r-score of 0.9 using Optuna
- Trained and fine-tuned GPT-2, Llama models on Aircraft Maintenance Manuals using SFT and PEFT techniques with 4 A100 GPUs
- Implemented RAG system with ChromaDB and OpenAI API for real-time AMM document creation, reducing manual effort by 80%
- Secured $200k funding through AI-driven document automation business value demonstration
- Led NLP-LLM community of practice, conducting 3 sessions on LLMs, RAG, and Generative AI
- Led hiring process for ML Engineers, successfully onboarding 6 candidates from 50 applicants

* At The Boeing Company in Bengaluru, I functioned in the Research and Operations wing of the Boeing Commercial Airplanes (BCA) division, focusing on developing future-generation automated production systems for factory settings.
* Pioneered algorithms to enhance operations procedure automation by training ML models within the Boeing Network, which included creating a Keyword Extraction Model using BERT with 95% accuracy for extracting crucial keywords from operations logs and a text summarization model using a fine-tuned T5 model achieving a Bleu-score of 25.
* Developed an intent detector and extractor utilizing semantic rules with NLTK, achieving 95% accuracy in extracting action items and intents from operation logs. Additionally, I played a key role in the recruitment process, leading the hiring of six associate ML Engineers from a pool of 50 candidates.
* At Boeing Research and Technology in Bengaluru, I developed a Generative AI-based solution for automating updates to Aircraft Maintenance Manuals using feedback from design engineers' Service bulletin messages. This involved parsing thousands of AMM documents from PDFs into text for Large Language Model (LLM) training.
* I fine-tuned custom GPT2 (medium) and GPTNeo models, pre-trained on domain-specific aerospace data, with subsequent multi-stage instruction fine-tuning using a prompt dataset formatted in alpaca, achieving 80% accuracy in generated authoring. Utilized 4 A100 GPUs on High Performance Computers (HPC) for optimized LLM training using PEFT, and RLHF techniques.

*  I created cost models for predicting airplane part prices in the Tear Down Analytics lab using Python. This involved automating training and evaluation workflows on tabular data exceeding 2 million rows, reducing modelling time by 70%. Employed threading and multiprocessing for hyperparameter tuning using Optune, training RandomForest Regressor and Xgboost models on HPC to achieve an average r-score of 90%.

Q. What is one ML project/experience that you want to highlight?

One experience I had working at Boeing was in training and developing a Generative AI solution for a technical publications team. As part of the problem statement, we had to create an automated bot or algorithm to generate new technical documents by ingesting old documents and relevant change drivers.

I had to parse over 2000 PDF documents containing technical content, tables, and diagrams. Initially, I tried using standard PDF parsers, but they weren’t working well. So, I created a custom parser that converts PDF documents to Markdown files and then extracts the necessary information using NLP techniques.

After collecting and structuring the dataset in the instruction-finetuning format, I approached the problem by first performing full fine-tuning of LLMs (I tried GPT-2 and Mistral-7B, among others). Then, I fine-tuned LORA and relevant tokenizers to adapt to the domain vocabulary. Finally, I created an end-to-end pipeline for automated training and validation.

After some testing, I implemented a Retrieval-Augmented Generation (RAG) system to improve the efficiency of text generation. I stored and retrieved context from ChromaDB and Langchain to support the RAG system and handle new data without the need for re-training. As a result, I was able to deliver a working prototype that generated new technical documents for different customer needs and use cases. This led to a significant reduction in manual effort, with an 80% decrease.

Company: Boeing Research and Technology - Data Scientist

* At Boeing Research and Technology in Bengaluru, I developed a Generative AI-based solution for automating updates to Aircraft Maintenance Manuals using feedback from design engineers' Service bulletin messages. This involved parsing thousands of AMM documents from PDFs into text for Large Language Model (LLM) training.
* I fine-tuned custom GPT2 (medium) and GPTNeo models, pre-trained on domain-specific aerospace data, with subsequent multi-stage instruction fine-tuning using a prompt dataset formatted in alpaca, achieving 80% accuracy in generated authoring. Utilized 4 A100 GPUs on High Performance Computers (HPC) for optimized LLM training using PEFT, and RLHF techniques.

*  I created cost models for predicting airplane part prices in the Tear Down Analytics lab using Python. This involved automating training and evaluation workflows on tabular data exceeding 2 million rows, reducing modelling time by 70%. Employed threading and multiprocessing for hyperparameter tuning using Optune, training RandomForest Regressor and Xgboost models on HPC to achieve an average r-score of 90%.

### Invento Robotics

**Software Engineering Intern** | *July 2021 - June 2022* | *Bengaluru, India*

    **• Developed the 'Invento Fleet' iOS app, allowing customers to control the robot remotely. Led the project and created over ten core app features using SwiftUI, Swift 5, and UIKit. Those 10 features include:

- Importuned Work Points:

1. Developed an API-based video calling feature from iPad to iPhone using TwilioVideo and TwilioAudio to establish communication between the Fleet manager and the Robot.
2. Implemented Socket-based communication between the iPhone app and the robot to trigger actions, manage the robot’s movement and send messages remotely.
3. Implemented live video communication from using the WebRTC technology to link bridge and connect the video being streamed from the robot to the iOS app.
4. Worked on the Human Fall Detection algorithm by developing a model to track whether the human has fallen or not using the Yolov5 object detection model.

- Worked on ROS-2 and iOS-based platforms to implement some key features to bridge the connectivity of the fleet portal and implement the same on the iOS app.
  • Gained over one year of experience building and deploying iOS applications to the App Store.
  • Developed audio-video communication infrastructure using TwilioVideo and WebRTCLib to reduce dependence on the Fleet Web portal by 90%. [Swift5, SwiftUI, WebRTC, Python, NodeJS]
  • Developed methodology for fail-proof for a fail-proof Fall Detection algorithm by rening a custom object detection model using the Yolov-v5 model as the base.
  • Reduced the number of 'True Negative' errors in fall detection by 95%.
  • Proficient in Python, PyTorch, MediaPipe, and ROS. 

**Software Developer Intern** | *July 2020 - August 2020* | *Bengaluru, India*

**• Maintained the content and performed testing of content for the Dialog Flow agent on the iOS app, including 100% client-specific data for demos and events.
• Built quality chatbots with strong NLP capabilities for robots using Dialogflow API.
• Reduced the time to create Dialogflow Intents and entities by 85% by automating the creation of intents and entities from client- specific content into a based interface.
• Created a script to automate data upload to the analytics server using Python3 and Selenium, reducing the time taken by 90\% %.
• Built a web app using Flask and Python3 to perform input validation and build conversational flows

## Projects

### AdVocate - Tartanhacks @ Carnegie Mellon University

*Feb 2025*

- Finalist for "Best Use of Generative AI" at TartanHacks 2025
- Engineered end-to-end AI marketing platform reducing campaign creation time by 90%
- Designed microservices architecture using Azure OpenAI, LangChain, and ChromaDB
- Optimized API costs with two-tier caching system, achieving 60% reduction in API calls
- Developed production-ready web application handling 50+ concurrent users

### Real-Time Options Trading Intelligence Platform

*Oct 2024 - Present*

- Developing options and derivatives prediction model combining statistical and neural network architectures
- Advanced options trading bot integrating real-time market data with sentiment-driven insights

### E-yantra Robotics Competition - Team Lead

*Sept 2020 - May 2021*

- Led 4-person team in developing automated warehouse system using ROS and Gazebo
- Optimized simulation performance by 50% through multi-threading
- Developed real-time package status website achieving competition score of 97.96/100

### NeuraForge - Publisher

*Aug 2023 - Present*

- Publishing a newsletter with content related Generative AI and ML

## Achievements & Awards

- Bureaucracy Crusher Award, SoCal Gemba Fest, Nov 2023 - Boeing Research & Technology
- CANDI Land Hackathon (Sept 2023) - Boeing Research & Technology
- GT TechFest Innovation Challenge (March 2023) - Boeing Research & Technology (Predictive Maintenance)
