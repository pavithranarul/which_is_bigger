import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Get the API key from an environment variable
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it as an environment variable.")

# Configure the Generative AI client
genai.configure(api_key=api_key)

# Create the model configuration
generation_config = {
    "temperature": 0.7,  # Lower temperature for deterministic responses
    "top_p": 0.9,       # Encourage likely responses
    "top_k": 50,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Initialize Flask app
app = Flask(__name__)

# Home route to serve the web interface
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle AI queries
@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    user_question = data.get("question", "").strip()

    if not user_question:
        return jsonify({"response": "Please enter a valid question."})

    try:
        # Start a new chat session with a prompt encouraging reasoning
        chat_session = model.start_chat(
            history=[
                {
                "role": "user",
                "parts": [
                    "What is bigger, 9.9 or 9.11?",
                ],
                },
                {
                "role": "model",
                "parts": [
                    "9.9 is bigger than 9.11.\n",
                ],
                },
            ]
            )

        # Send the user's question to the model
        response = chat_session.send_message(user_question)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)