import React from 'react'
import Editor from './components/Editor'

export default function App() {
  return (
    <div className="app-container">
      <header>
        <h1>Cursor AI</h1>
        <p>Describe what you want and get generated code.</p>
      </header>
      <main>
        <Editor />
      </main>
    </div>
  )
}
