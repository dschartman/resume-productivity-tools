import React, { useState } from 'react';

function ChatWindow() {
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Here you would handle sending the message to your backend
    alert(`Message to send: ${message}`);
    // After sending the message, clear the input
    setMessage('');
  };

  return (
    <div>
      <h2>Chat with our AI</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default ChatWindow;
