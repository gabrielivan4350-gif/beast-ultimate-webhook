from fastapi import FastAPI, Request
import os
import json

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "BEAST WEBHOOK LIVE"}

@app.post("/webhook")
async def helius_webhook(request: Request):
    try:
        data = await request.json()
        print("Webhook primit de la Helius:")
        print(json.dumps(data, indent=2))
        
        # AICI vei trimite datele către botul tău de pe PC (mai târziu)
        # Deocamdată doar loghează ca să vezi că merge
        
        return {"status": "ok"}
    except Exception as e:
        print("Eroare webhook:", e)
        return {"status": "error"}
