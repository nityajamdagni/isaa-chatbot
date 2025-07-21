
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 This line is CRITICAL


print("🟢 Starting Flask server...")

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from langchain.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = Flask(__name__)
CORS(app)  # ← This allows frontend (React) to talk to backend
# Flask app
app = Flask(__name__)
CORS(app)

# Load ISAA questions from JSON
with open("isaa_questions.json") as f:
    questions = json.load(f)

# LangChain + Ollama (using LLaMA 3)
llm = Ollama(model="llama3")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Simple session memory
sessions = {}

@app.route("/start", methods=["POST"])
def start_chat():
    session_id = request.json.get("session_id")
    sessions[session_id] = {
        "index": 0,
        "score": 0,
        "responses": []
    }
    return jsonify({
        "question": questions[0]["question"],
        "index": 0
    })

@app.route("/answer", methods=["POST"])
def handle_answer():
    data = request.json
    session_id = data["session_id"]
    score = int(data["score"])

    session = sessions[session_id]
    session["score"] += score
    session["responses"].append(score)
    session["index"] += 1

    i = session["index"]
    if i >= len(questions):
        total = session["score"]
        if total >= 70:
            result = "Severe Autism"
        elif total >= 50:
            result = "Moderate Autism"
        elif total >= 36:
            result = "Mild Autism"
        else:
            result = "No Autism"

        return jsonify({
            "done": True,
            "total": total,
            "result": result
        })

    return jsonify({
        "question": questions[i]["question"],
        "index": i
    })

@app.route("/explain", methods=["POST"])
def explain_question():
    data = request.json
    question = data["question"]
    prompt = f"Explain this ISAA autism screening question to a parent in simple terms: {question}"
    response = conversation.run(prompt)
    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)