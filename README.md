# LLM Security Chatbot

The LLM Security Chatbot is a cutting-edge tool designed to assist in understanding and researching cybersecurity vulnerabilities. Built with the powerful Llama Large Language Model (LLM) and integrated into a user-friendly interface using Streamlit, this chatbot leverages natural language processing to provide in-depth analysis, actionable insights, and potential mitigation strategies for a wide range of security concerns.

## Features

- **Interactive Chat Interface**: Engage in conversational queries and receive detailed responses.
- **Code Snippet Support**: Get examples and explanations with formatted code (still a work in progress) snippets for technical understanding.
- **Conversation History**: Review past queries and responses directly within the application.
- **Exportable Conversations**: Easily export the conversation history for documentation or further analysis.

## Getting Started

To get started with the LLM Security Chatbot, follow these steps:

### Prerequisites

Ensure you have Python 3.9+ installed on your system. You will also need the `streamlit` and `llama_cpp` packages.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jwalker/llm_security_chatbot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd llm_security_chatbot/
    ```
3. Install the required Python packages:
    ```bash
    uv pip install -r requirements.txt
    ```

### Running the Application

Launch the chatbot by running the Streamlit application:

```bash
streamlit run app.py
```

Visit http://localhost:8501 in your web browser to start interacting with the chatbot.

### Usage
Enter your cybersecurity-related queries in the text area and hit 'Submit' to receive a response. The chat interface allows for natural language questions and provides detailed explanations, including code examples when relevant.

### Contributing
Contributions are welcome! If you have suggestions for improvements or want to contribute to the development of the LLM Security Chatbot, please feel free to fork the repository and submit a pull request.

### Contact
If you have any questions or feedback, please reach out via email: jay@stellersjay.pub
