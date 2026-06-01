# **Charles Mareau's Portfolio**  

Welcome! This repository showcases some of my most interesting projects, demonstrating my skills in **Python, backend development, and full-stack web applications**.  

## 📌 **Projects**  

### **Climbing Statistics - Scraper** 
🔗 [Repository Link](https://github.com/charlesm-git/matchit-scraper)  
📊 An asynchronous Python scraper for **personal use only**, collecting data from the bleau.info website (40,000+ pages).
- **Async HTTP:** Uses `aiohttp` and `asyncio` for high-throughput scraping  
- **Database:** Stores most of publicly available information
- **Stack:** `Python, aiohttp, asyncio, SQLite, SQLAlchemy, Beautifulsoup`

---

### **Climbing Statistics - API**  
🔗 [Repository Link](https://github.com/charlesm-git/matchit-api)  
📈 A *FastAPI* backend serving climb statistics from the bleau.info dataset. Ideal for powering a React frontend with real-time charts and tables.  
- **RESTful Endpoints:** A large variety of endpoints for data retrievable. Easily customizable depending on Frontend needs
- **SQLAlchemy + Pydantic:** Clean CRUD layer with SQLAlchemy models and Pydantic schemas for validation  
- **Database (read-only):** Bundles the scraped SQLite file for read-only production use, with possible migration to PostgreSQL
- **Stack:** `Python, FastAPI, Pydantic, SQLite, SQLAlchemy`

---

### **Climbing Statistics - Front End**  
🔗 [Repository Link](https://github.com/charlesm-git/matchit-frontend)  
📊 A React-based web app providing interactive visualizations of climbing statistics from the Bleau.info API. Designed for smooth user experience and insightful data exploration.  
- **Dynamic Charts**: Uses Recharts for responsive line and bar charts showing trends and comparisons
- **State Management**: Efficiently handles data updates and UI state with React hooks
- **Stack:** `React, Vite, React Routing, Rechart, Tailwind` 
  
[Link to the demo frontend](https://matchit-frontend-13999527716.europe-west1.run.app)
- Recommendation system only works for the Ticino area for now.

---

### **Climbing Statistics - ML Models**  
🔗 [Repository Link](https://github.com/charlesm-git/bleauinfo-ML)  
🧠 Experimental machine learning models for exploring boulder similarity, recommendations, and pattern analysis from the bleau.info dataset.  
This repository serves as a staging ground for model prototyping before integration into the scraper or API layers.  
- **Similarity Models:** Sparse matrix-based Jaccard, Cosine, and domain-specific similarity techniques  
- **Pipeline Compatibility:** Outputs are used directly by the API or at data scraping time  
- **Performance-Driven:** Iterative testing for memory usage, computation speed, and model utility  
- **Stack:** `Python, NumPy, SciPy, scikit-learn, pandas`

--- 

### **Astat - Climbing Log & Stats App**  
🔗 [Repository Link](https://github.com/charlesm-git/Astat)  
📱 A mobile app designed for climbers to track their ascents, analyze performance, and create custom boulder to-do lists. Screenshots of the app are available directly on the repository.    
- **Fully local application** with offline functionality  
- **Built with Python & Kivy**  
- **Not released on app stores yet**  
- **Stack:** `Python, Kivy, SQLAlchemy`

---

Feel free to explore and reach out with any questions! 🚀  
