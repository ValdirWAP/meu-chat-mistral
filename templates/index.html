<!doctype html>
<html>
  <head>
    <title>Meu Chat iA (Valdir)</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background: #121212;
        color: #e0e0e0;
        padding: 20px;
        margin: 0;
      }
      h1 { color: #fff; }
      form {
        margin-bottom: 20px;
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
      }
      input[type="text"], select {
        flex: 1;
        padding: 10px;
        border-radius: 20px;
        border: 1px solid #333;
        background: #1e1e1e;
        color: #e0e0e0;
      }
      button {
        padding: 10px 15px;
        border-radius: 20px;
        border: none;
        background: #4CAF50;
        color: white;
        cursor: pointer;
      }
      button:hover { background: #45a049; }
      .chat-box {
        max-height: 400px;
        overflow-y: auto;
        background: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
      }
      .mensagem {
        display: flex;
        align-items: flex-start;
        margin: 10px 0;
        max-width: 80%;
      }
      .avatar {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        margin: 0 10px;
      }
      .texto {
        padding: 10px;
        border-radius: 15px;
        color: #fff;
        max-width: 100%;
      }
      .pergunta {
        background: #2e7d32;
        margin-left: auto;
        text-align: right;
      }
      .resposta {
        background: #424242;
        margin-right: auto;
        text-align: left;
        position: relative;
      }
      small {
        color: #aaa;
        font-size: 0.8em;
        display: block;
        margin-top: 5px;
      }
      .copy-btn {
        background: #2196F3;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 12px;
        margin-top: 5px;
      }
      .copy-btn:hover {
        background: #1976D2;
      }
      @media (max-width: 600px) {
        input[type="text"], select { font-size: 14px; }
        button { font-size: 14px; padding: 8px 12px; }
        .mensagem { max-width: 100%; }
      }
    </style>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  </head>
  <body>
    <h1>💬 Meu Chat iA Valdir</h1>

    <form method="post" action="/">
      <input type="text" name="prompt" placeholder="Digite sua pergunta" required>
      <select name="modelo">
        <option value="mistral-tiny">Mistral Tiny</option>
        <option value="mistral-small">Mistral Small</option>
        <option value="mistral-medium">Mistral Medium</option>
      </select>
      <button type="submit">Enviar</button>
    </form>

    <div class="botoes">
      <a href="/limpar"><button type="button">🧹 Limpar histórico</button></a>
    </div>

    <h2>Histórico:</h2>
    <div class="chat-box">
      {% for msg in historico %}
        <div class="mensagem pergunta">
          <div class="texto"><b>Você:</b> {{ msg.pergunta }} <br><small>{{ msg.hora }}</small></div>
          <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" class="avatar">
        </div>
        <div class="mensagem resposta">
          <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="avatar">
          <div class="texto">
            <b>Mistral ({{ msg.modelo }}):</b>
            <div class="markdown">{{ msg.resposta }}</div>
            <small>{{ msg.hora }}</small>
            <!-- Botão copiar -->
            <button class="copy-btn" onclick="copiarResposta(this)">Copiar resposta</button>
          </div>
        </div>
      {% endfor %}
    </div>

    <script>
      // Rolagem automática para última mensagem
      var chatBox = document.querySelector(".chat-box");
      chatBox.scrollTop = chatBox.scrollHeight;

      // Converter respostas para Markdown
      document.querySelectorAll(".markdown").forEach(function(el) {
        el.innerHTML = marked.parse(el.textContent);
      });

      // Função copiar resposta
      function copiarResposta(btn) {
        const resposta = btn.parentElement.querySelector(".markdown").innerText;
        navigator.clipboard.writeText(resposta).then(() => {
          btn.textContent = "Copiado!";
          setTimeout(() => btn.textContent = "Copiar resposta", 2000);
        });
      }
    </script>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Meu Chat iA</title>
</head>
<body>
    <h1>Bem-vindo, {{ usuario }}!</h1>

    <div style="margin-bottom: 20px;">
        <button onclick="window.location.href='/logout'">Logout</button>
    </div>

    <form action="/chat" method="post">
        <input type="text" name="prompt" placeholder="Digite sua pergunta..." required>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
