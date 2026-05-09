import React from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

function App() {
  return (
    <main>
      <h1>React Frontend</h1>
      <p>This is a second frontend app in the multi-frontend repository.</p>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
