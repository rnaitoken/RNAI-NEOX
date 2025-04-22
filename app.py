<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Integraciones con RNAI-NEOX</title>
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
    p {
      color: #ccc;
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
      transition: background 0.3s;
    }
    .api-box button:hover {
      background-color: #00cc77;
    }
    .message {
      font-size: 0.9rem;
      margin-top: 10px;
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
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <h1>Integraciones con RNAI-NEOX</h1>
  <p>Pega tus claves API o URLs de Webhook para activar funcionalidades automáticas.</p>

  <div class="api-container" id="form-list">
    <!-- Formularios generados dinámicamente -->
  </div>

  <script>
    const apis = [
      { nombre: "API de OpenAI", id: "openai", placeholder: "sk-xxxxx", endpoint: "https://api.openai.com/v1/chat/completions" },
      { nombre: "Webhook de Zapier", id: "zapier", placeholder: "https://hooks.zapier.com/hooks/xxx" },
      { nombre: "API de Zoom (JWT)", id: "zoom", placeholder: "eyJhbGciOi..." }
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

      localStorage.setItem(`api-${id}`, value);

      document.getElementById(`msg-${id}`).innerText = `✅ Clave guardada correctamente.`;
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
          document.getElementById(`msg-${id}`).innerText = `❌ Error de conexión: ${err.message}`;
        });
      }
    }
  </script>
</body>
</html>
