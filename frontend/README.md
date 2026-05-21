# Frontend (Cursor AI)

This is a minimal React + Vite frontend that allows you to send natural-language prompts to the Cursor AI backend and display the generated code.

Quick start (from repository root):

1. cd frontend
2. npm install
3. npm run dev

Notes:
- The frontend posts to the '/generate-code' endpoint. If your backend runs on a different origin, either enable CORS on the backend or set up a proxy during development.
