import requests
import json
import gradio as gr
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

# API URL from environment variables for security
URL = os.getenv("API_URL")

# HTTP headers
HEADERS = {
    'Content-Type': 'application/json'
}

# To store conversation history
history = []

def generate_response(prompt):
    """
    Sends the prompt to the model API and retrieves the response.
    
    Args:
    - prompt (str)

    Returns:
    - str: The model's response
    """
    try:
        history.append(prompt)
        final_prompt = "\n".join(history)

        # Data payload
        data = {
            "model": "my_custom_model",
            "prompt": final_prompt,
            "stream": False
        }

        # Sending the request to the API
        response = requests.post(URL, headers=HEADERS, data=json.dumps(data))

        # Handle success
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get('response', 'No response found')
        
        # Handle errors
        logging.error(f"Error {response.status_code}: {response.text}")
        return f"Error {response.status_code}: {response.text}"
    
    except Exception as e:
        logging.exception("An error occurred while generating the response.")
        return f"An error occurred: {str(e)}"

# Gradio Interface setup
def launch_interface():
    """
    Launches the interface.
    """
    interface = gr.Interface(
        fn=generate_response,
        inputs=gr.Textbox(lines=4, placeholder="Enter your prompt"),
        outputs="text",
        title="Chat with AI",
        description="Enter a prompt and interact with the custom AI model."
    )
    interface.launch()

if __name__ == "__main__":
    launch_interface()
