from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import subprocess  # Import subprocess to run the executable

app = Flask(__name__)
CORS(app)

def process_with_llama_cpp(query):
    # Define the prompt template with additional context
    prompt_template = """
    Q: {user_query}
    Context: The user is seeking in-depth analysis and actionable insights on cybersecurity vulnerabilities.
    You are well versed in C and C++ software development and understand the complexities of code audits in and out. 
    Please provide detailed information, potential mitigation strategies, and reference relevant tools or resources related to code audits from a cybersecurity perspective.
    A: """
    formatted_query = prompt_template.format(user_query=query)

    # Command to execute the llama.cpp main executable with the formatted query
    command = [
        '../../llama.cpp/main',  # Adjust the path to the executable as needed
        '-m', '../../llama.cpp/models/Meta-Llama-3-8B-Instruct/ggml-model-Q4_K_M.gguf',
        '-p', formatted_query,
        '-n', '400',
        '-e'
    ]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Extract the answer from the full response, if structured with an "A:" separator
        full_response = result.stdout.strip()
        answer_start_index = full_response.find('A:')
        if answer_start_index != -1:
            return full_response[answer_start_index + 2:].strip()  # Skip past "A:" itself
        return full_response
    else:
        return "Error in processing request: " + result.stderr.strip()

@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.json
    query = data.get('query')
    response = process_with_llama_cpp(query)  # Call the function that uses subprocess

    try:
        with open('conversation_history.json', 'r+') as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
            history.append({"query": query, "response": response})
            file.seek(0)
            json.dump(history, file)
            file.truncate()  # Truncate the file to the new content size
    except FileNotFoundError:
        with open('conversation_history.json', 'w') as file:
            json.dump([{"query": query, "response": response}], file)

    return jsonify({"response": response})

@app.route('/get_history', methods=['GET'])
def get_history():
    try:
        with open('conversation_history.json', 'r') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []

    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
