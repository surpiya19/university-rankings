import sqlite3
import pandas as pd

# Path to my SQLite database
DB_PATH = "data/university_database.db"


def run_query(query, params=None):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def execute_sql(sql, params=None):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # --- 1. Read: Top 5 universities in 2015 ---
    print("\nTop 5 universities in 2015:")
    q1 = """
    SELECT institution, country, world_rank, score
    FROM university_rankings
    WHERE year = 2015
    ORDER BY score DESC
    LIMIT 5;
    """
    print(run_query(q1))

    # --- 2. Read: Japanese universities in top 200 (2013) ---
    print("\nNumber of Japanese universities in top 200 (2013):")
    q2 = """
    SELECT COUNT(*) AS japan_top200
    FROM university_rankings
    WHERE country = 'Japan' AND year = 2013 AND world_rank <= 200;
    """
    print(run_query(q2))

    # --- 3. Insert: Duke Tech (2014) ---
    print("\nInserting Duke Tech (2014)...")
    insert_sql = """
    INSERT INTO university_rankings (institution, country, world_rank, score, year)
    VALUES (?, ?, ?, ?, ?)
    """
    execute_sql(insert_sql, ("Duke Tech", "USA", 350, 60.5, 2014))
    print("Inserted Duke Tech.")

    # --- 4. Update: Oxford 2014 score +1.2 ---
    print("\nUpdating University of Oxford (2014) score by +1.2...")
    update_sql = """
    UPDATE university_rankings
    SET score = score + 1.2
    WHERE institution = 'University of Oxford' AND year = 2014;
    """
    execute_sql(update_sql)
    print("Updated Oxford score.")

    # --- 5. Delete: Universities with score < 45 in 2015 ---
    print("\nDeleting universities with score < 45 in 2015...")
    delete_sql = """
    DELETE FROM university_rankings
    WHERE year = 2015 AND score < 45;
    """
    execute_sql(delete_sql)
    print("Deleted low-score universities in 2015.")

    # --- 6. Optional: View updated top 5 universities in 2015 ---
    print("\nUpdated top 5 universities in 2015:")
    print(run_query(q1))
