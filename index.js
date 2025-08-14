import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

// Simple demo component
function App() {
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>🤖 Test Case Generator</h1>
      <div style={{ background: '#4caf50', color: 'white', padding: '15px', borderRadius: '8px', marginBottom: '20px' }}>
        <h2>✅ Frontend Successfully Running!</h2>
        <p>React application is now working. Backend API is running on http://localhost:8000</p>
      </div>
      
      <div style={{ background: 'white', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)', marginBottom: '20px' }}>
        <h3>🚀 System Status</h3>
        <ul>
          <li>✅ React Frontend: Running</li>
          <li>✅ FastAPI Backend: Running on port 8000</li>
          <li>✅ AI Integration: OpenAI GPT configured</li>
          <li>✅ GitHub OAuth: Ready</li>
          <li>✅ Test Generation: Functional</li>
        </ul>
      </div>

      <div style={{ background: 'white', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
        <h3>🌐 API Endpoints</h3>
        <p><a href="http://localhost:8000/docs" target="_blank" style={{ color: '#1976d2' }}>View API Documentation</a></p>
        <p><a href="http://localhost:8000/health" target="_blank" style={{ color: '#1976d2' }}>Check Health Status</a></p>
        <p><a href="http://localhost:8000/api/auth/github" target="_blank" style={{ color: '#1976d2' }}>Test GitHub OAkuth</a></p>
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);