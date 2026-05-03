# 🏡 AreaHome — Smart Property Finder

A full-stack web application that converts natural language queries into intelligent property recommendations.

Example:
> "2BHK in ECIL under ₹20k, girl-friendly"

---

## ✨ Features

- 🔍 Natural language search → extracts BHK, budget, and location
- 🧠 Smart recommendation engine:
  - Exact match → higher → lower BHK prioritization
  - Nearby area fallback
  - Budget flexibility handling
- 🗺️ Interactive map with property markers
- 📊 Area scoring system (Safety, Water, IT proximity, Transport, etc.)
- 👩 Social-aware filtering (girl-friendly, bachelor-friendly, family)
- ⚡ Fast backend (no external API delays)

---

## 🛠 Tech Stack

**Frontend**
- React (Vite)
- Tailwind CSS
- MapLibre / Leaflet
- Chart.js

**Backend**
- FastAPI (Python)
- Async processing (asyncio)
- Custom scoring & ranking engine

---

## ⚙️ Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
