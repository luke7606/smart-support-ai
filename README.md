# 🤖 Smart Support AI

**EN:** Smart post-implementation support system that leverages AI modules, automated diagnostics, and technical dashboards.

**ES:** Sistema inteligente de soporte post-implementación con módulos de IA, diagnóstico automatizado y tableros técnicos.

---

## 🌐 Live demo / Demo en vivo

[smart-support-ai.vercel.app](https://smart-support-ai.vercel.app)

---

## ⚙️ Tech Stack

- 🐍 Python 3.x
- 🐳 Docker + Docker Compose
- 🚀 GitHub Actions (CI/CD)
- 📦 Streamlit (interfaz)
- 📊 JSON / PKL (datos estructurados y modelos)
- 🧠 IA básica + clasificación automatizada

---

## 🧠 Funcionalidades / Features

**ES:**

- Chat de soporte automatizado
- Diagnóstico de incidentes
- Revisión de logs y clasificación
- Generación de tickets internos
- Gestión de upgrades por módulo

**EN:**

- Automated support chatbot
- Incident diagnostics
- Log parsing and classification
- Internal ticket generation
- Upgrade tracking by module

---

## 🐳 Cómo correr localmente / Run locally

```bash
# Clonar el repo
git clone git@github.com:lucasmera/smart-support-ai.git
cd smart-support-ai

# Opción 1: con Docker
docker-compose up --build

# Opción 2: modo dev sin Docker
pip install -r requirements.txt
streamlit run app.py

