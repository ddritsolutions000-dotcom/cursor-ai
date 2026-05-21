import React, { useState } from 'react'
import axios from 'axios'

export default function Editor() {
  const [prompt, setPrompt] = useState('')
  const [result, setResult] = useState('')
  const [loading, setLoading] = useState(false)

  const submit = async () => {
    if (!prompt) return
    setLoading(true)
    setResult('')
    try {
      // Assumes backend is served from the same origin or a proxy is configured
      const res = await axios.post('/generate-code', { prompt })
      setResult(res.data.generated_code || JSON.stringify(res.data, null, 2))
    } catch (err) {
      setResult('Error: ' + (err.response?.data?.detail || err.message))
    }
    setLoading(false)
  }

  return (
    <div className="editor">
      <textarea
        placeholder="e.g. Create a Flask API that returns 'Hello World'"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows={8}
        cols={80}
      />
      <div>
        <button onClick={submit} disabled={loading || !prompt}>
          {loading ? 'Generating...' : 'Generate Code'}
        </button>
      </div>
      <div className="output">
        <h3>Generated Code</h3>
        <pre>{result}</pre>
      </div>
    </div>
  )
}
