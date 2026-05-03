# 🏡 AreaHome — AI-Powered Property Recommendation Platform

A full-stack intelligent rental search system that converts natural language queries into personalized, location-aware property recommendations.

> 💬 Example:
> **"2BHK in ECIL under ₹20k, girl-friendly"**

---

## 🚀 Overview

AreaHome redefines property search by replacing traditional filters with natural language understanding.

The system extracts user intent (budget, BHK, location, lifestyle preferences) and ranks properties using a **custom multi-factor scoring engine**, delivering highly relevant results in real time.

---

## ✨ Key Features

### 🔍 Natural Language Search

* Parses queries like humans speak
* Extracts:

  * Budget constraints
  * BHK requirements
  * Preferred locations
  * Social preferences
* Handles flexible and incomplete inputs

---

### 🧠 Intelligent Recommendation Engine

* Priority-based ranking system:

  * Exact BHK match → highest priority
  * Higher/lower BHK fallback when needed
* Smart fallback when no exact matches:

  * Nearby areas
  * Similar pricing range
* Context-aware filtering

---

### 🗺️ Interactive Map Experience

* Real-time property markers
* Area-based visualization
* Nearby amenities (schools, hospitals, etc.)
* Seamless sync with property list

---

### 📊 Multi-Factor Scoring System

Each property is evaluated using:

* 💧 Water Supply
* 🛡️ Safety
* 💼 IT Hub Proximity
* 🏫 Schools
* 🚇 Transport
* 🌳 Greenness
* 🌤️ Weather

👉 Combined into a **single ranked score (0–100)**

---

### 👩 Social-Aware Recommendations

* Girl-friendly locality scoring
* Bachelor-friendly filtering
* Family-oriented area detection
* Society-type awareness

---

### ⚡ Performance Optimizations

* Async backend processing (FastAPI + asyncio)
* Removed slow external API dependencies
* Optimized scoring pipeline for fast responses

---

## 🛠️ Tech Stack

### Frontend

* React (Vite)
* Tailwind CSS
* Leaflet / MapLibre
* Chart.js

### Backend

* FastAPI (Python)
* AsyncIO (concurrent processing)
* Custom recommendation & scoring engine

### Data Layer

* JSON-based property dataset
* Precomputed area intelligence scores

---

## 📸 Screenshots

### 🏠 Home Page — Natural Language Search

![Home](./screenshots/home.png)

---

### 📊 Results Page — Map + Listings + AI Scoring

![Results](./screenshots/results.png)

---

### ⏳ Loading Flow — Intelligent Processing

![Loading](./screenshots/loading.png)

---

## ⚙️ Local Setup

### 🔹 Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🔹 Frontend

```bash
cd frontend
npm install
npm run dev
```

👉 Open: http://localhost:5173

---

## 🧠 System Design Highlights

* Built a **custom recommendation engine** (not just filtering)
* Implemented **multi-level fallback logic** (BHK + area + budget)
* Designed a **weighted scoring system** across 6+ parameters
* Introduced **social-context-aware ranking**
* Optimized backend using **async concurrency**
* Reduced latency by replacing heavy external APIs

---

## 🚀 Future Improvements

* Database integration (MySQL / PostgreSQL)
* Geo-distance-based ranking
* Real-time APIs (weather, amenities)
* User authentication & personalization
* Full cloud deployment with scalability

---

## 📌 Project Status

* ✅ Fully functional (local)
* ✅ Production-ready architecture
* 🔜 Deployment in progress

---

## 👨‍💻 Author

**Mohd Sameer**
🔗 GitHub: https://github.com/mohdsameer18n

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
