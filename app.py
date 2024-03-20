import streamlit as st
from llama_cpp import Llama

# Initialize the Llama model
llm = Llama(
    model_path="../llama.cpp/models/mistral-7B-v0.1/ggml-model-Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
    chat_format="chatml"
)

st.set_page_config(page_title="💬 Security ChatBot")
st.title('Security ChatBot - Ask me something')

if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []
if 'debug_info' not in st.session_state:
    st.session_state['debug_info'] = {}

user_query = st.text_area("Enter your query related to cybersecurity research", '')

prompt_template = """
Q: {user_query}
Context: The user is seeking in-depth analysis and actionable insights on cybersecurity vulnerabilities. 
Please provide detailed information, potential mitigation strategies, and reference relevant tools or resources.
A: """

def display_conversation():
    """
    Display the conversation history with the most recent messages first.
    Format messages appropriately, including code blocks.
    """
    for exchange in st.session_state['conversation_history']:
        # Check for the type of exchange to handle string-only history entries gracefully
        if isinstance(exchange, dict):
            message, sender = exchange['message'], exchange['sender']
        else:  # Fallback for string entries, assuming all older entries are from the user
            message, sender = exchange, 'User'
        
        # Format message as Markdown to properly display code blocks and maintain line breaks
        if sender == 'Agent' and '```' in message:
            # Assuming code blocks are enclosed in triple backticks
            st.markdown(f"**{sender}:**\n```{message.split('```')[1]}```", unsafe_allow_html=True)
        else:
            st.markdown(f"**{sender}:**\n{message}", unsafe_allow_html=True) # clearly not safe

def display_debug_info():
    if st.session_state['debug_info']:
        st.json(st.session_state['debug_info'])

def export_conversation_history():
    with open('conversation_history.txt', 'w') as file:
        for exchange in reversed(st.session_state['conversation_history']):
            if isinstance(exchange, dict):
                line = f"{exchange['sender']}: {exchange['message']}\n"
            else:
                line = f"User: {exchange}\n"
            file.write(line)
    st.success('Conversation exported successfully!')

if st.button('Submit'):
    if user_query:
        st.session_state['conversation_history'].append({"sender": "Researcher", "message": user_query})
        with st.spinner('Analyzing your query...'):
            prompt = prompt_template.format(user_query=user_query)
            output = llm(prompt, max_tokens=2048, stop=["Q:"], echo=True)
            
            if 'choices' in output and len(output['choices']) > 0:
                raw_response = output['choices'][0]['text']
                user_friendly_response = raw_response.split('A: ')[-1].strip()
                
                st.session_state['conversation_history'].append({"sender": "Agent", "message": user_friendly_response})
                st.session_state['debug_info'] = output
            else:
                st.error("The model did not return a valid response. Please try again.")
    else:
        st.warning("Please enter a query.")

display_conversation()
# Sidebar for additional controls
with st.sidebar:
    st.image('https://files.oaiusercontent.com/file-TAKOjgzaq5efA7OIusxh2Vkw?se=2024-03-20T06%3A55%3A23Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dbf88bd85-a472-465b-8707-3d315307bc9b.webp&sig=CuqICRvq4pHQ45NGIxADC5AcIjrzdutbcrrYLKA73AY%3D', width=100)  # Consider adding a logo or related visual
    st.markdown('## 🛠 Controls & Tools')
    st.markdown("""---""") 

    # Reset Conversation Button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button('🔄', help='Reset Conversation'):
            st.session_state.conversation_history = []
            st.session_state.debug_info = {}
    with col2:
        st.markdown("**Reset Conversation**")

    # Export Conversation History Button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button('💾', help='Export Conversation History'):
            export_conversation_history()
    with col2:
        st.markdown("**Export Conversation History**")

    # Show Debug Information Button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button('🐛', help='Show Debug Information'):
            display_debug_info()
    with col2:
        st.markdown("**Show Debug Information**")
    
    st.markdown("""---""")  # Horizontal line for visual separation
    
    # Link to Blog Post
    st.markdown('📖 [Blog post on setup and how the app was built](https://blog.stellersjay.pub)')

    st.markdown("---")  # Horizontal line for visual separation
    st.markdown("## 📬 Contact & Source Code")
    
    # GitHub Repo Link
    st.markdown("Check out the [GitHub repository](https://github.com/jwalker/your-repo-name) for this project.")
    
    # Email Contact
    st.markdown("Feel free to reach out via email: [jwalker](mailto:jay@stellersjay.pub)")

