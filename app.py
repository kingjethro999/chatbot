from flask import Flask, request, jsonify, send_file
from chatbot import CloudLLaMAChatbot
import os
app = Flask(__name__)
# Initialize the chatbot
api_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_token:
raise Exception("Please set the HUGGINGFACE_API_TOKEN environment variable.")
chatbot = CloudLLaMAChatbot(api_token)
@app.route('/')
def home():
return send_file('index.html') # Serve the index.html file from the root
@app.route('/chat', methods=['POST'])
def chat():
user_input = request.json.get('message')
if not user_input:
return jsonify({'error': 'Message is required'}), 400
response = chatbot.generate_response(user_input)
return jsonify({'response': response})
if __name__ == '__main__':
app.run(debug=True)

from flask_lambda import FlaskLambda
app = FlaskLambda(app)