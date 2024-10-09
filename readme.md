# Custom Gemma 2b Chatbot

This project implements a chatbot using a customized codellama 7b, quantized to 4bit precision, served through Ollama API, and presented with a Gradio interface.

## Overview

This chatbot leverages the power of the codellama 7b language model, fine-tuned to act as a python code teaching assistant.


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/custom-gemma-chatbot.git
   cd custom-gemma-chatbot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the environment variable:
   - Create a `.env` file in the project root
   - Add the following line: `API_URL=http://localhost:11434/api/generate`


## Custom Model Configuration

The custom model is configured using the `modelfile` with the following settings:

- Base model: codellama:7b-code-q4_0
- Temperature: 1
- System prompt: Configured to act as a code assistant created by Khalil

