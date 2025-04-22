# 📦 RNAI-NEOX Dashboard - Integrador de APIs

Este proyecto forma parte del ecosistema de **RNAI-NEOX Genesis Pro**, una arquitectura modular que permite:

- Integración de APIs mediante formularios no-code
- Guardado seguro y automático de claves en backend
- Validación de conexiones activas (como OpenAI)
- Expansión a nuevos servicios y bots autónomos

---

## ⚙️ ¿Qué incluye este proyecto?

- `api.html`: Panel web con formularios dinámicos para integrar hasta 10 APIs populares
- `api/save.js`: Endpoint backend que guarda claves en `api_keys.json`
- `api_keys.json`: Archivo de claves centralizado (se genera automáticamente)
- `deploy_rnai_backend.js`: Script de despliegue completo

---

## 🔌 APIs disponibles

| Servicio        | ID           | Tipo      |
|----------------|--------------|-----------|
| OpenAI         | `openai`     | API Key   |
| Zapier         | `zapier`     | Webhook   |
| Zoom           | `zoom`       | JWT       |
| ElevenLabs     | `elevenlabs` | API Key   |
| Telegram       | `telegram`   | Webhook   |
| Twilio         | `twilio`     | SID Token |
| WhatsApp Cloud | `whatsapp`   | Webhook   |
| Gemini AI      | `gemini`     | API Key   |
| Discord        | `discord`    | Bot Token |
| HuggingFace    | `huggingface`| API Key   |

---

## 🛠 Cómo usar

### 1. Subir archivos a tu repositorio (GitHub):

Coloca estos archivos en la raíz del proyecto:

```
/README.md
/api/save.js
/api_keys.json  ← se crea automáticamente
/api.html
/deploy_rnai_backend.js
```

> 📌 Consejo: Asegúrate que `/api/save.js` sea accesible como endpoint si usas Vercel.

### 2. Despliega en Vercel o Railway

- **Vercel:** Usar `/dashboard` como carpeta raíz para interfaces como `api.html`
- **Railway:** Ideal para la lógica backend (guardar claves, lógica del bot, etc)

### 3. Abre `api.html` desde tu dashboard

- Coloca tu API key en el formulario correspondiente
- Pulsa "Ejecutar"
- El sistema guardará y validará la conexión
- Verás confirmación visual + hora de guardado

---

## 🌐 URLs sugeridas

- Panel: `https://tuusuario.vercel.app/api.html`
- Backend: `https://tuusuario.vercel.app/api/save`

---

## 🧠 Sobre RNAI-NEOX

RNAI-NEOX es el núcleo maestro del enjambre digital autónomo, creado para gestionar bots, módulos IA y operaciones descentralizadas. Este dashboard es el primer paso hacia el ecosistema de bots-crías, con control remoto e inteligencia operativa modular.

---

## 📩 Contacto

Creado por [RNAI Core](mailto:genesis.rnai@gmail.com) con ❤️ para el futuro autónomo.

---

¡Activa tus APIs y que comience la revolución digital! 🚀

