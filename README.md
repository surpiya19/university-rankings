# university-database
This repository explores relational databases and CRUD operations using SQLite and Python (pandas). It includes a pre-built SQLite database (university_database.db) containing university ranking data from 2012–2015.

The project runs in a reproducible Dev Container environment with all dependencies and tools (Python, SQLite, and Plotly) preinstalled.

---

## 🚀 Features

- SQLite database integration and exploration via **SQL** and **Python**
- SQL-based CRUD operations (Create, Read, Update, Delete)
- Data analysis and visualization with Plotly
- Ready-to-use Dev Container for seamless setup
- Includes helper scripts to run and visualize queries (`scripts/query.py`)

---

## 🧩 Dev Container Setup

The .devcontainer configuration ensures the environment is **always ready** — no manual installs are required.
##### 🔧 Includes
- Python 3.12
- SQLite3 CLI
- pandas, plotly, sqlite-utils
- VS Code SQLite extensions preinstalled

---

## Project Structure
```markdown
university-database/
│
├── .devcontainer/
│   ├── devcontainer.json            # Defines container environment and VS Code extensions
│   ├── docker-compose.yml           # Configures service and volume for the Dev Container
│   └── Dockerfile                   # Installs Python, SQLite, and dependencies
│
├── data/
│   └── university_database.db       # Pre-built SQLite database (2012–2015 rankings)
│
├── scripts/
│   ├── query.py                     # Performs CRUD operations on the database
│   ├── crud_ops.sql                 # SQL version of CRUD operations
│   ├── additional_analysis.py       # Generates visualizations and extended analysis
│   └── test_conn.py                 # Verifies database connection
│
├── visualizations/
│   ├── top_countries_top100.html           # Top 10 countries by top-100 universities
│   ├── score_distribution_top10_countries.html  # Score distributions for top 10 countries
│   └── score_change_2014_2015.html         # Universities with largest score changes
│
├── requirements.txt                 # Python dependencies (pandas, plotly, sqlite-utils)
└── README.md                        # Project overview and documentation
```
---

## DB Connection Test:

```bash
import sqlite3

try:
    conn = sqlite3.connect("data/university_database.db")
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("Connected successfully. Tables:", cur.fetchall())
    conn.close()
except Exception as e:
    print("Connection failed:", e)

```
Outputs:
![alt text](<screenshots/Screenshot 2025-10-06 at 4.53.46 PM.png>)
![SQLite Viewer](<screenshots/Screenshot 2025-10-06 at 4.57.12 PM.png>)

---

## 🧱 Project Architecture

Here’s how everything connects inside the Dev Container:

```mermaid
flowchart TD

    subgraph DevContainer["VS Code Dev Container"]
        A[scripts/query.py] -->|CRUD queries| B[(data/university_database.db)]
        A --> C[pandas DataFrame]
        C --> D[visualizations/*.html]
        E[scripts/additional_analysis.py] -->|Analytical queries + Plotly| B
        E --> D
    end

    B -.->|Database interactions| A
    B -.->|Data retrieval| E
    DevContainer --> F[GitHub Repository]
```
---

## Viewing Visualizations
After running `python scripts/additional_analysis.py`, open the generated HTML files in your browser:

```bash
open visualizations/top_countries_top100.html
open visualizations/score_distribution_top10_countries.html
open visualizations/score_change_2014_2015.html
```

---

## Visualization
**1. Score distributions across the top 10 countries:**
![alt text](<screenshots/Screenshot 2025-10-06 at 5.08.06 PM.png>)

**2. Top countries having their universities in top 100**
![alt text](<screenshots/Screenshot 2025-10-06 at 5.09.20 PM.png>)

**3. Score change from 2014 -> 2015 in top 10 countries**
![alt text](<screenshots/Screenshot 2025-10-06 at 5.10.58 PM.png>)

---