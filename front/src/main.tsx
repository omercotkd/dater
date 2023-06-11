import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import 'shoppa-ui/styles/_index.scss'
import "./App.css"

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
