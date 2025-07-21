# 🧠 ISAA Autism Screening Chatbot

An intelligent, full-stack chatbot that conducts the **Indian Scale for Assessment of Autism (ISAA)** screening for children, guiding parents through 40 structured questions and providing a final assessment.

---

## 💡 Features

- ✅ Step-by-step ISAA screening with 40 questions
- 🧠 Uses LLaMA 3 (via Ollama + LangChain) to **explain questions** in simple language
- 📊 Calculates the autism level based on total score
- 💬 Friendly React-based chatbot interface
- 🔁 Restart anytime
- 🌈 Responsive UI and clean scoring guide
- 🧾 Easily extendable to export PDF or save data

---

## 🚀 Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Frontend   | React.js                    |
| Backend    | Flask (Python)              |
| LLM Agent  | LangChain + Ollama (LLaMA 3)|
| PDF Parser | PyMuPDF                     |
| Hosting    | (Localhost / GitHub)        |

---

## 📦 Project Structure
isaa-chatbot/
│
├── backend/ # Flask API with LangChain + Ollama
│ ├── app.py
│ ├── extract_questions.py
│ └── isaa_questions.json
│
├── frontend/ # React chatbot UI
│ ├── src/
│ ├── public/
│ └── package.json
│
└── README.md


---

## 🧠 ISAA Scoring Guide

| Score | Meaning             |
|-------|---------------------|
| 1     | Rarely (0–20%)      |
| 2     | Sometimes (21–40%)  |
| 3     | Frequently (41–60%) |
| 4     | Mostly (61–80%)     |
| 5     | Always (81–100%)    |

---

## 🚀 How to Run Locally

### ▶️ 1. Start Backend

```bash
cd backend
python app.py 
ollama run llama3

cd frontend
npm install
npm start


Then open: http://localhost:3000