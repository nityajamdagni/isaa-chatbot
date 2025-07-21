import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [sessionId] = useState('parent-session-001');
  const [question, setQuestion] = useState('');
  const [index, setIndex] = useState(0);
  const [result, setResult] = useState(null);
  const [explanation, setExplanation] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    startTest();
  }, []);

  const startTest = async () => {
    const res = await axios.post('http://localhost:5000/start', { session_id: sessionId });
    setQuestion(res.data.question);
    setIndex(res.data.index);
    setResult(null);
    setExplanation('');
  };

  const handleAnswer = async (score) => {
    setLoading(true);
    const res = await axios.post('http://localhost:5000/answer', {
      session_id: sessionId,
      score: score
    });

    if (res.data.done) {
      setResult(res.data.result);
      setQuestion('');
    } else {
      setQuestion(res.data.question);
      setIndex(res.data.index);
    }

    setExplanation('');
    setLoading(false);
  };

  const handleExplain = async () => {
    setLoading(true);
    const res = await axios.post('http://localhost:5000/explain', {
      question: question
    });
    setExplanation(res.data.response);
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>🧠 Autism Screening Chatbot (ISAA)
      <div className="scale-guide">
  <h3>📊 ISAA Scoring Guide</h3>
  <ul style={{ textAlign: "left", paddingLeft: "20px" }}>
    <li>1 – Rarely (0–20%)</li>
    <li>2 – Sometimes (21–40%)</li>
    <li>3 – Frequently (41–60%)</li>
    <li>4 – Mostly (61–80%)</li>
    <li>5 – Always (81–100%)</li>
  </ul>
</div>
</h1>

      {result ? (
        <div>
          <h2>✅ Screening Complete</h2>
          <p><strong>Result:</strong> {result}</p>
          <button onClick={startTest}>Start Again</button>
        </div>
      ) : (
        <>
          <h2>Q{index + 1}: {question}</h2>

          <div className="buttons">
            {[1, 2, 3, 4, 5].map(score => (
              <button key={score} onClick={() => handleAnswer(score)} disabled={loading}>
                {score}
              </button>
            ))}
          </div>

          <button onClick={handleExplain} disabled={loading || !question}>
            🤔 Explain This Question
          </button>

          {loading && <p>Thinking...</p>}
          {explanation && (
            <div className="explanation">
              <strong>Explanation:</strong> {explanation}
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default App;
