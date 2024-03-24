const backendUrl = process.env.REACT_APP_BACKEND_URL;

export const generateText = async (prompt, conversationHistory) => {
  try {
    const response = await fetch(`http://localhost:8000/generate-text/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, conversation_history: conversationHistory }),
    });
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  } catch (error) {
    console.error('Error during API call:', error);
    throw error;
  }
};
