<template>
  <div class="chatbox">
    <div class="messages">
      <div v-for="(item, index) in conversationHistory" :key="index" class="message">
        <p><strong>Researcher:</strong> {{ item.query }}</p>
        <br>
        <p><strong>Bot (soon agent):</strong></p>
        <p v-html="formatMessage(item.response)"></p>
      </div>
    </div>
    <div class="form-container">
      <textarea v-model="userQuery" ref="messageInput" rows="3" @keyup.enter="sendQuery" placeholder="Ask something..."></textarea>
      <button @click="sendQuery">Send</button>
    </div>
  </div>

</template>

<script>
// Import the logo image
import logo from '@/assets/chatbot.jpg';

import axios from 'axios';

export default {
  name: 'SecurityChatBox', // Updated name to be multi-word
  data() {
    return {
      userQuery: '',
      conversationHistory: [],
      logo,
    };
  },
  methods: {
    sendQuery() {
      if (!this.userQuery) return;
      this.loading = true;
      axios.post('http://127.0.0.1:5000/submit_query', { query: this.userQuery })
        .then(() => { // Changed to underscore since response is not directly used
          this.fetchHistory(); // Refresh the history to include the new conversation
          this.userQuery = ''; // Clear the input field
          this.$refs.messageInput.focus();
          this.scrollToBottom();
        })
        .catch(error => console.error(error));
    },
    fetchHistory() {
      axios.get('http://127.0.0.1:5000/get_history')
        .then(response => {
          this.conversationHistory = response.data;
          this.scrollToBottom();
        })
        .catch(error => console.error(error));
    },
    // Add to the methods in <script>
    scrollToBottom() {
      this.$nextTick(() => {
        const messagesContainer = this.$el.querySelector(".messages");
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      });
    },
    formatMessage(message) {
      // Format code blocks: Replace triple backticks with <pre><code> tags
      let formattedMessage = message.replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>').replace(/\[([^\]]+)]\((http[s]?:\/\/[^\s]+?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

      // Basic attempt to format C code snippets without explicit backtick fencing
      // This example looks for lines containing #include or void ...() and formats the whole paragraph as a code block
      // Warning: This is a simplistic heuristic and may not accurately identify all code snippets
      formattedMessage = formattedMessage.split('\n').map(line => {
        if (line.includes('#include') || (/void\s+\w+\(.*\)/.test(line))) {
          return '<pre><code>' + line + '</code></pre>';
        } else {
          return line;
        }
      }).join('\n');
      // Format unordered lists: Replace lines starting with "* " with <li> tags, wrapped in <ul>
      formattedMessage = formattedMessage.replace(/^\* (.*?)(?=\n|$)/gm, '<li>$1</li>')
                                          .replace(/(<li>.*?<\/li>)/gs, '<ul>$1</ul>');

      // Format ordered lists: Replace lines starting with "1. " or any number followed by ". "
      formattedMessage = formattedMessage.replace(/^\d+\. (.*?)(?=\n|$)/gm, '<li>$1</li>')
                                          .replace(/(<li>.*?<\/li>)/gs, '<ol>$1</ol>');

      // Optional: Format headers if used in your responses
      // For example, simple handling for H2 headers
      formattedMessage = formattedMessage.replace(/^## (.*?)(?=\n|$)/gm, '<h2>$1</h2>');

      // Add this line for Markdown link conversion
      formattedMessage = formattedMessage.replace(/\[([^\]]+)]\((http[s]?:\/\/[^\s]+?)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');

      // Further enhancements here based on observed formatting needs

      return formattedMessage;
    }

  },
  mounted() {
    this.fetchHistory(); // Fetch the conversation history when the component is mounted
  }
};
</script>

<style>

/* Add to the <style> section of SecurityChatBox.vue */
.chatbox {
  display: flex;
  flex-direction: column;
  max-width: 600px;
  height: 80vh; /* Adjust based on your preference */
  margin: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  background-color: #f9f9f9;
}

.messages {
  overflow-y: auto;
  padding: 20px;
  flex-grow: 1;
}

.message {
  margin-bottom: 20px;
  background-color: #fff;
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-container {
  border-top: 1px solid #ccc;
  background-color: #fff;
  display: flex;
  padding: 10px;
}


.message p {
  margin: 0;
  color: #333;
}

input, button {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin: 10px;
}

button {
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
}

/* Further styling within <style> */
input {
  flex-grow: 1;
  margin-right: 10px;
}

button:hover {
  background-color: #0056b3;
}

/* Flex container for input and button */
.form-container {
  display: flex;
  padding: 0 20px 20px;
}

/* Defined user vs bot */
.user-message {
  text-align: right;
}

.bot-message {
  text-align: left;
}

/* Responsiveness */
@media (max-width: 768px) {
  .chatbox {
    width: 95%;
    margin: 10px auto;
  }

  .messages, .form-container {
    padding: 10px;
  }
}

/* Add or update in your <style> section */
textarea {
  width: 100%; /* Ensure it fills the container */
  resize: vertical; /* Allow vertical resizing, restrict horizontal resizing */
  margin-right: 10px; /* Maintain spacing between textarea and send button */
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 10px;
}

/* Add some styles for the logo */
.chatbot-logo {
  width: 100px; /* Or whatever size you prefer */
  height: auto;
  display: block; /* Center the logo if needed */
  margin: 0 auto; /* Center the logo horizontally */
}
</style>
