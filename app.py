from flask import Flask, request, render_template, redirect, url_for
import requests, json, os
from datetime import datetime


MAX_CONTEXT = 10  # número de mensagens de contexto
cache = {}
CACHE_FILE = "cache.json"

# Carregar cache existente
try:
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)
except FileNotFoundError:
    cache = {}

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "segredo-super-seguro"


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
        modelo = request.form.get("modelo", "mistral-tiny")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario == "valdir" and senha == "1234":
            session["usuario"] = usuario
            return redirect("/")
        else:
            return "Login inválido!"
    return '''
        <form method="post">
            Usuário: <input type="text" name="usuario"><br>
            Senha: <input type="password" name="senha"><br>
            <input type="submit" value="Entrar">
        </form>
    '''
@app.route("/")
def home():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return f"Bem-vindo, {session['usuario']}! Este é o chat protegido."
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


        # Construir lista de mensagens com histórico limitado
mensagens = []
for msg in historico[-MAX_CONTEXT:]:
    mensagens.append({"role": "user", "content": msg["pergunta"]})
    mensagens.append({"role": "assistant", "content": msg["resposta"]})

# Adicionar a nova pergunta
mensagens.append({"role": "user", "content": prompt})

if prompt in cache:
    # Se já existe resposta no cache, usa ela
    resposta = cache[prompt]
else:
    # Construir lista de mensagens com histórico limitado
    mensagens = []
    for msg in historico[-MAX_CONTEXT:]:
        mensagens.append({"role": "user", "content": msg["pergunta"]})
        mensagens.append({"role": "assistant", "content": msg["resposta"]})

    mensagens.append({"role": "user", "content": prompt})
if prompt in cache:
    resposta = cache[prompt]
else:
    # monta mensagens e chama API normalmente
    ...
    resposta = data["choices"][0]["message"]["content"]

   MAX_CACHE = 100  # número máximo de entradas no cache

# Salva no cache em memória
cache[prompt] = resposta

# Se o cache passar do limite, remove a entrada mais antiga
if len(cache) > MAX_CACHE:
    # remove o primeiro item inserido
    chave_antiga = next(iter(cache))
    del cache[chave_antiga]

# Grava em arquivo
with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)


    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": modelo,
        "messages": mensagens
    }
    response = requests.post(BASE_URL, headers=headers, json=data)
    data = response.json()

    if "choices" in data:
        resposta = data["choices"][0]["message"]["content"]
    else:
        resposta = f"Erro na resposta da API: {data}"

    # Salva no cache
    cache[prompt] = resposta


        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": modelo,
            "messages": mensagens
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
    # Render usa gunicorn, mas localmente você pode rodar com Flask
    app.run(host="0.0.0.0", port=5000, debug=True)
