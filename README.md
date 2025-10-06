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

The .devcontainer configuration ensures your environment is **always ready** — no manual installs are required.
##### 🔧 Includes
- Python 3.12
- SQLite3 CLI
- pandas, plotly, sqlite-utils
- VS Code SQLite extensions preinstalled

---

## Project Structure

.
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── data/
│   └── university_database.db
├── scripts/
│   ├── query.py
│   ├── crud_ops.sql
│   └── additional_analysis.py
├── visualizations/
│   ├── top_countries_top100.html
│   ├── score_distribution_top10_countries.html
│   └── score_change_2014_2015.html
├── requirements.txt
└── README.md

---

## DB Connection:

```
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
![Connection](<Screenshot 2025-10-06 at 4.53.46 PM.png>)

![SQLite Viewer](<Screenshot 2025-10-06 at 4.57.12 PM.png>)

---

## 🧱 Project Architecture

Here’s how everything connects inside the Dev Container:

```mermaid
flowchart TD

    subgraph DevContainer["VS Code Dev Container 🐳"]
        A[📜 scripts/query.py] -->|CRUD queries| B[(💾 data/university_database.db)]
        A --> C[pandas DataFrame]
        C --> D[📊 visualizations/*.html]
        E[📜 scripts/additional_analysis.py] -->|Analytical queries + Plotly| B
        E --> D
    end

    B -.->|Database interactions| A
    B -.->|Data retrieval| E
    DevContainer --> F[🌐 GitHub Repository]
