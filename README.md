# **Charles Mareau's Portfolio**

Software engineer based in **Copenhagen**, focused on **backend development, data pipelines, and AI/LLM integration**. Mechanical-engineering background (MSc, INSA Lyon), software-development degree (BSc, OpenClassrooms), currently full-stack engineer at an ESG/compliance SaaS startup.

**Main stack:** `Python (FastAPI, Pydantic, SQLAlchemy)` · `TypeScript/React` · `PostgreSQL` · `Docker, Azure, GCP`

Below are the projects I built on my own time, grouped by the kind of work they show.

---

## 🤖 **AI & Automation**

### **Job Searcher - Automated Job Search & CV Tailoring**
🔗 [Repository Link](https://github.com/charlesm-git/job-searcher)
A local daily pipeline that scrapes the last 24h of LinkedIn postings, scores each one for relevance with an LLM, tailors a CV and cover letter for the good matches, and writes a daily report into an Obsidian vault.
- **Two-Stage LLM Pipeline:** A cheap relevance pre-filter runs on every posting, expensive tailoring only on the ones that pass — keeping token usage minimal
- **Prompt Engineering:** Scoring driven by a structured candidate profile with explicit penalty rules, tuned iteratively to cut false positives
- **Scraping & Dedup:** Guest-endpoint scraping (no login) with conservative throttling and SQLite-based deduplication across runs
- **Fully Automated:** Scheduled daily via a macOS LaunchAgent, running end-to-end without interaction
- **Stack:** `Python, requests, BeautifulSoup, SQLite, PyYAML, Claude CLI`

---

## ⚙️ **Backend & Data Engineering**

The three projects below form a single end-to-end system: **scrape → store → serve → visualize** climbing statistics from a 100,000+ page dataset.

### **Climbing Statistics - Scraper**
🔗 [Repository Link](https://github.com/charlesm-git/matchit-scraper)
An asynchronous Python scraper for **personal use only**, collecting data from the 8a.nu website (100,000+ pages).
- **Human-Like Behavior:** Strong rate limiting and static headers via session management to simulate natural user behavior and avoid bot detection
- **Database:** Stores most of the publicly available information
- **Stack:** `Python, requests, PostgreSQL, SQLAlchemy, BeautifulSoup`

### **Climbing Statistics - API**
🔗 [Repository Link](https://github.com/charlesm-git/matchit-api)
A *FastAPI* backend serving climb statistics from the 8a.nu dataset, powering the React frontend with real-time charts and tables.
- **RESTful Endpoints:** A large variety of endpoints for data retrieval, easily customizable depending on frontend needs
- **SQLAlchemy + Pydantic:** Clean CRUD layer with SQLAlchemy models and Pydantic schemas for validation
- **Deduplication Logic:** Intelligent merging of duplicate boulder ascents to maintain data integrity and consistency
- **Stack:** `Python, FastAPI, Pydantic, PostgreSQL, SQLAlchemy`

---

## 💻 **Full-Stack & Applications**

### **Climbing Statistics - Front End**
🔗 [Repository Link](https://github.com/charlesm-git/matchit-frontend) · 🚀 [Live demo](https://matchit-frontend-13999527716.europe-west1.run.app)
A React web app providing interactive visualizations of climbing statistics served by the API above.
- **Dynamic Charts:** Recharts-based responsive line and bar charts showing trends and comparisons
- **State Management:** Efficiently handles data updates and UI state with React hooks
- **Admin Panel:** Data management interface featuring deduplication logic to merge and clean duplicate boulder records
- **Stack:** `React, Vite, React Router, Recharts, Tailwind`

*Note: the recommendation system only covers the Ticino area for now.*

### **Astat - Climbing Log & Stats App**
🔗 [Repository Link](https://github.com/charlesm-git/Astat)
A mobile app for climbers to track their ascents, analyze performance, and create custom boulder to-do lists. Screenshots are available directly on the repository.
- **Fully local application** with offline functionality
- **Not released on app stores yet**
- **Stack:** `Python, Kivy, SQLAlchemy`

---

Feel free to explore and reach out with any questions! 🚀
