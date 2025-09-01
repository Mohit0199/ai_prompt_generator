# AI Prompt Generator

## Overview

**AI Prompt Generator** is an intelligent tool that transforms simple, natural language inputs into polished, structured, and role-based prompts optimized for use with any Large Language Model (LLM). Built with Streamlit and powered by LangChain and Ollama's qwen2.5 model, this application helps users create high-quality prompts across various domains such as coding, marketing, storytelling, analysis, and education.

The tool automatically enriches user inputs with:
- **Role assignments** (e.g., "You are an expert...")
- **Formatting rules** (bullet points, numbered steps, structured output)
- **Constraints and instructions** (detail level, style, tone, audience)
- **Tone adaptations** (Professional, Casual, Humorous, Persuasive)

Whether you're a developer, marketer, educator, or content creator, this app simplifies the process of crafting effective prompts for AI interactions.

## Features

- **User-Friendly Interface**: Clean Streamlit web app with an intuitive sidebar and main content area.
- **Tone Selection**: Choose from four distinct tones to tailor the output style:
  - **Professional**: Detailed, structured, and benefit-focused.
  - **Casual**: Simple, relatable, with everyday examples.
  - **Humorous**: Fun, light, with witty analogies.
  - **Persuasive**: Benefit-driven, motivational, with calls-to-action.
- **Local LLM Integration**: Leverages Ollama for offline, privacy-focused AI processing.
- **Customizable Models**: Easily switch between different Ollama models (default: qwen2.5:latest).
- **Copy-Paste Ready**: Outputs directly usable prompts in a code block format.
- **Domain Agnostic**: Works for any topic or use case, from technical coding to creative writing.
- **Extensible Architecture**: Modular design with separate engine and prompt template files for easy customization.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8+**: Download from [python.org](https://www.python.org/downloads/).
- **Ollama**: A tool for running LLMs locally. Download and install from [ollama.ai](https://ollama.ai/).
  - After installation, pull the required model: `ollama pull qwen2.5:latest` (or your preferred model).
- **Git**: For cloning the repository (optional, if not downloading directly).

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-prompt-generator.git
   cd ai-prompt-generator
   ```

2. **Set Up a Virtual Environment** (Recommended):
   ```bash
   python -m venv myvenv
   # On Windows:
   myvenv\Scripts\activate
   # On macOS/Linux:
   source myvenv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Ollama Setup**:
   - Ensure Ollama is running: `ollama serve`
   - Confirm the model is available: `ollama list`

## Usage

1. **Start the Application**:
   ```bash
   streamlit run app.py
   ```
   - The app will open in your default web browser at `http://localhost:8501`.

2. **Interact with the App**:
   - **Sidebar**: Read the about section for tips and usage guidelines.
   - **Main Area**:
     - Enter your idea, task, or request in the text area (e.g., "Write a LinkedIn post about AI in healthcare").
     - Select your preferred tone from the radio buttons.
     - Click **"🚀 Generate Optimized Prompt"**.
   - **Results**: The optimized prompt will appear in a code block below. Copy it directly for use in any LLM.

3. **Example Workflow**:
   - Input: "Help me write Python code to sort a list."
   - Tone: Professional
   - Output: A fully structured prompt like: "You are a Python programming assistant. Task: Write efficient Python code to sort a list of numbers. Requirements: ..."

4. **Customization**:
   - To change the LLM model, edit `engine.py` and update the `model_name` parameter in the `PromptEngine` class (e.g., to "llama2:latest").
   - Modify the prompt template in `prompt.py` for advanced customizations.

## Dependencies

The project relies on the following key libraries (from `requirements.txt`):

- **streamlit**: For the web interface.
- **langchain**: Core framework for LLM interactions.
- **langchain-ollama**: Integration with Ollama models.

## Project Structure

```
ai-prompt-generator/
├── app.py              # Main Streamlit application
├── engine.py           # PromptEngine class for LLM processing
├── prompt.py           # Expert prompt engineer template
```


