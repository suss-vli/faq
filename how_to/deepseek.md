---
layout: default
title: DeekSeek R1
parent: How-To
nav_order: 1
permalink: deepseek/
---

# FAQ - DeepSeek R1
{: .no_toc }

If your issue cannot be resolved by any of the FAQ, please email <bryanlimyt@suss.edu.sg> for assistance. <!-- <vlisupport@suss.edu.sg> -->

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## What is DeepSeek R1
DeepSeek R1 is an advanced reasoning AI model developed by the Chinese company DeepSeek, designed to excel at complex problem-solving and logical tasks by breaking down issues into multiple steps; it is considered a competitor to OpenAI's models and is notable for being open-source, allowing for free commercial and academic use, while also boasting a lower operating cost compared to other high-performance AI models. 

Key points about DeepSeek R1:
- **Focus on reasoning:** Unlike many other AI models that prioritize generating text, DeepSeek R1 prioritizes logical reasoning and step-by-step problem-solving. 
- **Open-source access:** The model is available to the public under an MIT license, allowing researchers and developers to freely access and customize it. 
- **Cost-effective:** Compared to other high-performance AI models, DeepSeek R1 is designed to operate at a significantly lower cost. 
- **Reinforcement learning based:** The model leverages reinforcement learning techniques to improve its reasoning capabilities. 
- **Potential applications:** Complex problem-solving, logical inference tasks, research projects requiring advanced reasoning abilities. 

## Running DeepSeek Locally
To run DeepSeek R1 locally, follow any of these options:
1. **Running Model Locally using Ollama**
    - Guide by CodeAcademy: [How to Run Deepseek R1 Locally](https://www.codecademy.com/article/how-to-run-deepseek-r-1-locally)
    - Guide by WorkOS: [How to run DeepSeek locally](https://workos.com/blog/how-to-run-deepseek-r1-locally)

  **Choosing a Distilled Model**: The DeepSeek-R1-Distill variants are smaller (1.5B, 7B, 8B, etc.) and optimized for developers/students/lecturers who: 
  - Want lighter compute requirements, so they can run models on less-powerful machines. 
  - Prefer faster responses, especially for real-time coding help. 
  - Don’t want to sacrifice too much performance or reasoning capability.
  
  To install a distilled model (e.g. 1.5b), just specify its tag, as such: 
  `ollama run deepseek-r1:1.5b`

  **Integrations with R1 Model**
  - Visual Studio Code Extension: **CodeGPT**
    - [Link to Guide](https://x.com/dani_avila7/status/1884041492697600173)
  - **Open WebUI** - Simple web-based interface for interacting with Ollama models 
    - [Link to Open WebUI](https://openwebui.com/)
    - [Link to GitHub Repository](https://github.com/open-webui/open-webui)
  - **Gradio**: Query and analyze documents with DeepSeek-R1
    - [Link to Guide](https://www.datacamp.com/tutorial/deepseek-r1-ollama#running-a-local-gradio-app-for-rag-with-deepseek-r1)
  - **Docker**: Run DeepSeek-R1 in a Docker container
    - [Link to Guide](https://medium.com/@nirajranasinghe/running-deepseek-r1-locally-with-ollama-and-docker-9b2b7d05607a)

2. **Running Model Locally using LM Studio**
[![How to Install DeepSeek Locally on Windows from Scratch
](https://img.youtube.com/vi/G5BDBYQAJEs/0.jpg)](https://www.youtube.com/watch?v=G5BDBYQAJEs)

3. **Running Model Locally using llama.cpp**
https://huggingface.co/unsloth/DeepSeek-R1-GGUF

