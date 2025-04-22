<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Integraciones RNAI-NEOX - Dashboard</title>
  <style>
    body {
      background-color: #111;
      color: #fff;
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 20px;
    }
    h1 {
      color: #00ff99;
    }
    .api-container {
      margin-top: 20px;
      width: 100%;
      max-width: 600px;
    }
    .api-box {
      background-color: #222;
      padding: 20px;
      margin-bottom: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px #00ff9966;
      position: relative;
    }
    .api-box h3 {
      margin-bottom: 10px;
      color: #00ff99;
    }
    .api-box input {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: none;
      border-radius: 5px;
    }
    .api-box button {
      background-color: #00ff99;
      color: #000;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .message {
      font-size: 0.9rem;
      color: #00ff99;
    }
    .timestamp {
      font-size: 0.8rem;
      color: #999;
    }
    .toggle-visibility {
      position: absolute;
      top: 48px;
      right: 15px;
      background: none;
      border: none;
      color: #00ff99;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Integraciones RNAI-NEOX</h1>
  <div class="api-container" id="form-list"></div>

  <script>
    const apis = [
      { nombre: "API de OpenAI", id: "openai", placeholder: "sk-xxxxx", endpoint: "https://api.openai.com/v1/chat/completions" },
      { nombre: "Webhook de Zapier", id: "zapier", placeholder: "https://hooks.zapier.com/hooks/xxx" },
      { nombre: "API de Zoom (JWT)", id: "zoom", placeholder: "eyJhbGciOi..." },
      { nombre: "API de ElevenLabs", id: "elevenlabs", placeholder: "eleven-xxxxx" },
      { nombre: "Webhook de Telegram Bot", id: "telegram", placeholder: "https://api.telegram.org/botxxxxx/sendMessage" },
      { nombre: "API de Twilio", id: "twilio", placeholder: "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" },
      { nombre: "Webhook de WhatsApp Cloud API", id: "whatsapp", placeholder: "https://graph.facebook.com/v16.0/xxxx/messages" },
      { nombre: "API de Gemini AI", id: "gemini", placeholder: "AIzaSyD..." },
      { nombre: "API de Discord Bot", id: "discord", placeholder: "Bot MTAx..." },
      { nombre: "API de HuggingFace", id: "huggingface", placeholder: "hf_abcdefg..." }
    ];

    const formList = document.getElementById("form-list");

    apis.forEach(api => {
      const box = document.createElement("div");
      box.className = "api-box";

      const title = document.createElement("h3");
      title.innerText = api.nombre;
      box.appendChild(title);

      const input = document.createElement("input");
      input.type = "password";
      input.placeholder = api.placeholder;
      input.id = `input-${api.id}`;
      box.appendChild(input);

      const toggleBtn = document.createElement("button");
      toggleBtn.className = "toggle-visibility";
      toggleBtn.innerText = "👁️";
      toggleBtn.onclick = () => {
        input.type = input.type === "password" ? "text" : "password";
        toggleBtn.innerText = input.type === "password" ? "👁️" : "🙈";
      };
      box.appendChild(toggleBtn);

      const btn = document.createElement("button");
      btn.innerText = "Ejecutar";
      btn.onclick = () => ejecutarAPI(api.id, input.value, api.endpoint);
      box.appendChild(btn);

      const msg = document.createElement("p");
      msg.className = "message";
      msg.id = `msg-${api.id}`;
      box.appendChild(msg);

      const time = document.createElement("p");
      time.className = "timestamp";
      time.id = `time-${api.id}`;
      box.appendChild(time);

      formList.appendChild(box);
    });

    function ejecutarAPI(id, value, endpoint) {
      if (!value) return;
      const now = new Date();
      const timestamp = now.toLocaleString();

      fetch('/api/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: id, key: value })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById(`msg-${id}`).innerText = `✅ ${data.message}`;
        document.getElementById(`time-${id}`).innerText = `Última actualización: ${timestamp}`;

        if (id === "openai" && endpoint) {
          fetch(endpoint, {
            method: "POST",
            headers: {
              "Authorization": `Bearer ${value}`,
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              model: "gpt-3.5-turbo",
              messages: [{ role: "user", content: "¿Estás activo?" }]
            })
          })
          .then(res => res.json())
          .then(data => {
            if (data.choices) {
              document.getElementById(`msg-${id}`).innerText += " Respuesta recibida ✅";
            } else {
              document.getElementById(`msg-${id}`).innerText += " Pero hubo un error en la respuesta. ❌";
            }
          })
          .catch(err => {
            document.getElementById(`msg-${id}`).innerText = `❌ Error conexión OpenAI: ${err.message}`;
          });
        }
      })
      .catch(err => {
        document.getElementById(`msg-${id}`).innerText = `❌ Error guardando en backend: ${err.message}`;
      });
    }
  </script>
</body>
</html>
