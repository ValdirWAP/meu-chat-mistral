from flask import Flask, request, render_template, redirect, url_for
import requests, json, os
from datetime import datetime

app = Flask(__name__)

# Pega a chave da Mistral do ambiente (Render → Environment Variables)
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.mistral.ai/v1/chat/completions"
ARQUIVO = "conversas.json"

# Carregar histórico se já existir
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        historico = json.load(f)
else:
    historico = []

@app.route("/", methods=["GET", "POST"])
def chat():
    global historico
    if request.method == "POST":
        prompt = request.form["prompt"]
        modelo = request.form.get("modelo", "mistral-tiny")  # padrão tiny
        print("Recebi:", prompt, "Modelo:", modelo)

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": modelo,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(BASE_URL, headers=headers, json=data)
        data = response.json()

        if "choices" in data:
            resposta = data["choices"][0]["message"]["content"]
        else:
            resposta = f"Erro na resposta da API: {data}"

        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

        historico.append({
            "pergunta": prompt,
            "resposta": resposta,
            "hora": timestamp,
            "modelo": modelo
        })

        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)

    return render_template("index.html", historico=historico)

@app.route("/limpar")
def limpar():
    global historico
    historico = []
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True)
