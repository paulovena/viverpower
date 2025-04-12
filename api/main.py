from fastapi import FastAPI
from pydantic import BaseModel
import os, psycopg2
from datetime import datetime
import requests

app = FastAPI()

# Conexão com banco de dados PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# Controle de sessões por telefone
sessions = {}

class WebhookData(BaseModel):
    phone: str
    message: str

@app.post("/webhook")
async def webhook(data: WebhookData):
    phone = data.phone
    message = data.message.strip()
    step = sessions.get(phone, {}).get("step", 1)

    if step == 1:
        sessions[phone] = {"step": 2, "recipient_name": message}
        return {"reply": "Digite o telefone do destinatário:"}

    elif step == 2:
        sessions[phone]["step"] = 3
        sessions[phone]["recipient_phone"] = message
        return {"reply": "Digite a mensagem que deseja enviar:"}

    elif step == 3:
        info = sessions.pop(phone)
        recipient_name = info["recipient_name"]
        recipient_phone = info["recipient_phone"]

        # Armazena no banco de dados
        cursor.execute(
            "INSERT INTO powers (sender_phone, recipient_name, recipient_phone, message, created_at) VALUES (%s, %s, %s, %s, %s)",
            (phone, recipient_name, recipient_phone, message, datetime.now())
        )
        conn.commit()

        # Envia mensagem via API Evolution
        requests.post(f"https://api.serverviver.cloud/message/sendText/{os.getenv('EVOLUTION_INSTANCE_NAME')}", json={
            "number": recipient_phone,
            "options": {"delay": 1200, "presence": "composing"},
            "textMessage": {"text": message}
        }, headers={"apikey": os.getenv("EVOLUTION_TOKEN")})

        return {"reply": f"✅ Power enviado para {recipient_name} com sucesso!"}
