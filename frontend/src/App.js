import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");
  const submit = async () => {
    try {
      const request = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          prompt: prompt,
          max_tokens: 100,
          temperature: 0.7
        })
      });
      const data = await request.json();
      console.log((data));
      setResult(data.result);
    } catch (error) {
      setResult("Server error")
      console.log("Server error: ", error);
    }
  }
  return (
    <div>
      <div class="Submit-form">
        <textarea
          class="Text-area"
          value={prompt}
          onChange={(e) => { setPrompt(e.target.value) }}>
        </textarea>
        <button onClick={submit}>
          Submit
        </button>
      </div>
      {result && (
        <>
          <h2>Result:</h2>
          <pre>{result}</pre>
        </>
      )}
    </div>
  );
}

export default App;
