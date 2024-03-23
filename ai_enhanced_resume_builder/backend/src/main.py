import os
import openai
from fastapi import FastAPI, HTTPException

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/generate-text/")
async def generate_text(prompt: str):
    try:
        response = openai.Completion.create(
            engine="gpt-4-0125-preview",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
