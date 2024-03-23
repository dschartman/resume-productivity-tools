import React, { useState } from 'react';
import { generateText } from './services/api';


function ChatWindow() {
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!message.trim()) return;

        try {
            const response = await generateText(message);
            alert(`Generated text: ${response.response}`);
            setMessage('');
        } catch (error) {
            console.error('Failed to generate text:', error);
        }
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
