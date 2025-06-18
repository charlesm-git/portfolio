# **Charles Mareau's Portfolio**  

Welcome! This repository showcases some of my most interesting projects, demonstrating my skills in **Python, backend development, and full-stack web applications**.  

## 📌 **Projects**  

### **Astat - Climbing Log & Stats App**  
📱 A mobile app designed for climbers to track their ascents, analyze performance, and create custom boulder to-do lists.  
- **Fully local application** with offline functionality  
- **Built with Python & Kivy**  
- **Not released on app stores yet**  
- **Stack:** `Python, Kivy, SQLAlchemy`

🔗 More details & code snippets available in the **Astat folder**  

---

### **Bleau.info Scraper** 
🔗 [Repository Link](https://github.com/charlesm-git/bleauinfo-scraper)  
📊 An asynchronous Python scraper for **personal use only**, collecting data from the bleau.info website (40,000+ pages).
- **Async HTTP:** Uses `aiohttp` and `asyncio` for high-throughput scraping  
- **Database:** Stores most of publicly available information
- **Stack:** `Python, aiohttp, asyncio, SQLite, SQLAlchemy`


---

### **Bleau.info Statistics API**  
🔗 [Repository Link](https://github.com/charlesm-git/bleauinfo-api)  
📈 A *FastAPI* backend serving climb statistics from the bleau.info dataset. Ideal for powering a React frontend with real-time charts and tables.  
- **RESTful Endpoints:** A large variety of endpoints for data retrievable. Easily customizable depending on Frontend needs
- **SQLAlchemy + Pydantic:** Clean CRUD layer with SQLAlchemy models and Pydantic schemas for validation  
- **Database (read-only):** Bundles the scraped SQLite file for read-only production use, with possible migration to PostgreSQL
- **Stack:** `Python, FastAPI, Pydantic, SQLite, SQLAlchemy`

---
### **Bleau.info Statistics Front End**  
🔗 [Repository Link](https://github.com/charlesm-git/bleauinfo-frontend)  
📊 A React-based web app providing interactive visualizations of climbing statistics from the Bleau.info API. Designed for smooth user experience and insightful data exploration.  
*Currently being developed, subject to major changes.*
- **Dynamic Charts**: Uses Recharts for responsive line and bar charts showing trends and comparisons
- **State Management**: Efficiently handles data updates and UI state with React hooks
- **Stack:** `React, Vite, React Routing, Rechart, Tailwind` 


---

### **Django REST API - Project & Issue Tracker**  
🔗 [Repository Link](https://github.com/charlesm-git/API_Django_REST)  
A RESTful API for managing projects, contributors, issues, and comments. Implements authentication with JWT and custom permission management.  
- **Stack:** `Python, Django REST Framework, JWT` 

---

### **Django Book Review Web App**  
🔗 [Repository Link](https://github.com/charlesm-git/LitRevu_Django_App)  
A simple web app where users can post and review books. Features authentication, CRUD operations, and a minimal front-end with HTML & CSS.  
- **Stack:** `Python, Django, HTML, CSS`

---

Each project highlights different aspects of my development expertise, from **mobile app development** to **REST API design** and **full-stack web applications**.  

Feel free to explore and reach out with any questions! 🚀  
