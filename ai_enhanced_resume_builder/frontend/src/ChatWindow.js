import React, { useState } from 'react';
import { generateText } from './services/api';

function ChatWindow() {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMessage = { role: 'user', content: input };
        const updatedMessages = [...messages, userMessage];
        setMessages(updatedMessages);
        setInput('');

        try {
            const response = await generateText(input, messages);
            const assistantMessage = response.response;
            setMessages([...updatedMessages, assistantMessage]);
        } catch (error) {
            console.error('Failed to generate text:', error);
        }
    };

    return (
        <div>
            <h2>Chat with our AI</h2>
            <div className="chat-messages">
                {messages.map((message, index) => (
                    <div key={index} className={`message ${message.role}`}>
                        {message.content}
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message here..."
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}

export default ChatWindow;