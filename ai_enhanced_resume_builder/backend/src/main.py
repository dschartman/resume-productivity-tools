import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException

app = FastAPI()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.post("/generate-text/")
async def generate_text(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return {"response": response.choices[0].message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
