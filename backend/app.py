from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from llama_cpp import Llama

app = Flask(__name__)
CORS(app)

llm = Llama(
    model_path="../../llama.cpp/models/mixtral-8x7B/ggml-model-Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
    chat_format="chatml"
)

def process_with_model(query):
    
    prompt_template = """
    Q: {user_query}
    Context: The user is seeking in-depth analysis and actionable insights on cybersecurity vulnerabilities. 
    Please provide detailed information, potential mitigation strategies, and reference relevant tools or resources.
    A: """

    formatted_query = prompt_template.format(user_query=query)

    response = llm(formatted_query, max_tokens=2048, stop=["Q:"], echo=True)
    
    full_response = response['choices'][0]['text'].strip()

    # Extract only the answer part after "A:"
    answer_start_index = full_response.find('A:')
    if answer_start_index != -1:
        # +2 to skip past "A:" itself
        answer = full_response[answer_start_index + 2:].strip()
    else:
        answer = full_response  # Fallback to the full response if "A:" is not found

    return answer

@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.json
    query = data.get('query')
    response = process_with_model(query)

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
