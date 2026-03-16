from flask import Flask, render_template, request, jsonify
from chatbot import ContextAwareChatbot
import os

app = Flask(__name__)

# Resolving absolute path to the knowledge base so it runs from any directory
base_dir = os.path.dirname(os.path.abspath(__name__))
kb_path = os.path.join(base_dir, 'knowledge_base.json')

# Initialize single global instance of our chatbot.
chatbot = ContextAwareChatbot(kb_path)

@app.route('/')
def index():
    """
    Renders the web UI.
    """
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    """
    REST API endpoint for the chatbot.
    Receives JSON with a 'message' field and returns the chatbot's response.
    """
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided."}), 400
        
    user_message = data['message']
    
    # Process through our pipeline
    result = chatbot.get_response(user_message)
    
    return jsonify(result)

@app.route('/api/reset', methods=['POST'])
def reset_endpoint():
    """
    Clears the chatbot memory context.
    """
    chatbot.reset_session()
    return jsonify({"status": "Session context reset."})

if __name__ == '__main__':
    # Run server locally on port 5000
    app.run(debug=True, port=5000)
