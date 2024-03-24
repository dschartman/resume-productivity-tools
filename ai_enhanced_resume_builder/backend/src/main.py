import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


class GenerateTextRequest(BaseModel):
    prompt: str


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.post("/generate-text/")
async def generate_text(request: GenerateTextRequest):
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
                    "content": request.prompt,
                },
            ],
        )
        return {"response": response.choices[0].message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
