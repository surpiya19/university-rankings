# university-database
This repository explores relational databases and CRUD operations using SQLite and Python (pandas). It includes a pre-built SQLite database (university_database.db) containing university ranking data from 2012–2015.

The project runs in a reproducible Dev Container environment with all dependencies and tools (Python, SQLite, and Plotly) preinstalled.

---

## 🚀 Features

- SQLite database integration and exploration
- SQL-based CRUD operations (Create, Read, Update, Delete)
- Data analysis and visualization with Plotly
- Ready-to-use Dev Container for seamless setup
- Includes helper scripts to run and visualize queries

---

## 🧩 Dev Container Setup

The .devcontainer configuration ensures your environment is **always ready** — no manual installs are required.
##### 🔧 Includes
- Python 3.12
- SQLite3 CLI
- pandas, plotly, sqlite-utils

---

## 🧱 Project Architecture

Here’s how everything connects inside the Dev Container:

```mermaid
flowchart TD

    subgraph DevContainer["VS Code Dev Container 🐳"]
        A[query.py] -->|executes SQL| B[(university_database.db)]
        A --> C[pandas DataFrame]
        C --> D[Plotly Visualizations 📊]
    end

    B -.->|CRUD operations| A
    DevContainer --> E[GitHub Repository 🌐]
