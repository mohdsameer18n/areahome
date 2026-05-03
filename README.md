# 🏡 AreaHome — Smart Property Recommendation Platform

A full-stack web application that converts natural language queries into intelligent, location-aware property recommendations.

> Example:
> **"2BHK in ECIL under ₹20k, girl-friendly"**

---

## 🚀 Overview

AreaHome simplifies house hunting by allowing users to search using natural language instead of filters.
It intelligently extracts user intent (budget, BHK, location, preferences) and ranks properties using a custom scoring engine.

---

## ✨ Features

### 🔍 Smart Search

* Natural language parsing (BHK, budget, area)
* Flexible query understanding
* Supports real-world queries

### 🧠 Intelligent Recommendation Engine

* Priority-based ranking:

  * Exact BHK match → Higher → Lower fallback
* Nearby area suggestions when no exact match
* Budget flexibility handling

### 🗺️ Interactive Map UI

* Property markers with clustering
* Nearby amenities visualization
* Real-time selection sync

### 📊 Score-Based Decision System

Each property is evaluated on:

* Water Supply
* Safety
* IT Hub proximity
* Schools
* Transport
* Greenness
* Weather

### 👩 Social-Aware Filtering

* Girl-friendly areas
* Bachelor-friendly properties
* Family-preferred societies

### ⚡ Optimized Performance

* Async backend processing
* Removed heavy API delays for fast response

---

## 🛠 Tech Stack

### Frontend

* React (Vite)
* Tailwind CSS
* Leaflet / MapLibre
* Chart.js

### Backend

* FastAPI (Python)
* AsyncIO for concurrency
* Custom scoring & ranking engine

### Data

* JSON-based property dataset
* Area-based scoring system

---

## 📸 Screenshots

### 🏠 Home Page — Natural Language Search

![Home](./screenshots/home (2).png)

### 📊 Results Page — Map + Property Listings + Scores

![Results](./screenshots/results.png)

### ⏳ Loading Experience — Smart Processing Flow

![Loading](./screenshots/loading.png)

---

## ⚙️ Run Locally

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

* Designed a **custom recommendation engine** instead of simple filtering
* Implemented **fallback strategies** (nearby areas + flexible pricing)
* Built a **multi-factor scoring model** combining 6+ parameters
* Optimized performance by **removing slow external API dependencies**
* Used **async processing** for faster backend responses

---

## 🚀 Future Improvements

* Database integration (MySQL / PostgreSQL)
* Distance-based ranking using geolocation
* Real-time APIs (weather, amenities)
* Authentication & user preferences
* Full deployment with scalable backend

---

## 📌 Project Status

✅ Fully functional locally
✅ Clean GitHub repository
🔜 Deployment in progress

---

## 👨‍💻 Author

**Mohd Sameer**
GitHub: https://github.com/mohdsameer18n

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps!
