from fastapi import FastAPI
import openai, os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/ask")
def ask_agent(q: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":q}]
    )
    return {"answer": response.choices[0].message["content"]}
