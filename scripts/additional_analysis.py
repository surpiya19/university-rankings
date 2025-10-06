import sqlite3
import pandas as pd
import plotly.express as px

DB_PATH = "data/university_database.db"


def run_query(query, params=None):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


if __name__ == "__main__":
    print("\n--- Bonus Analysis with Enhanced Visualizations ---")

    # --- Top 10 countries by universities in top 100 ---
    q_top_countries = """
    SELECT country, COUNT(*) AS top100_count
    FROM university_rankings
    WHERE world_rank <= 100
    GROUP BY country
    ORDER BY top100_count DESC
    LIMIT 10;
    """
    df_top_countries = run_query(q_top_countries)
    print(df_top_countries)

    # Enhanced bar chart for top countries
    fig1 = px.bar(
        df_top_countries,
        x="country",
        y="top100_count",
        text="top100_count",
        color="top100_count",
        color_continuous_scale="Viridis",
        title="Top 10 Countries by Universities in Top 100",
    )
    fig1.update_layout(yaxis_title="Number of Universities", xaxis_title="Country")
    fig1.write_html("top_countries_top100_pretty.html")

    # --- Score distribution for top 10 countries ---
    top_countries_list = df_top_countries["country"].tolist()
    q_scores = f"""
    SELECT country, score
    FROM university_rankings
    WHERE country IN ({','.join(['?']*len(top_countries_list))})
      AND score IS NOT NULL
    """
    df_scores = run_query(q_scores, top_countries_list)

    fig2 = px.box(
        df_scores,
        x="country",
        y="score",
        points=False,
        color="country",
        title="Score Distribution for Top 10 Countries",
    )
    fig2.update_layout(yaxis_title="Score", xaxis_title="Country", showlegend=False)
    fig2.write_html("score_distribution_top10_countries.html")

    # --- Top 10 universities with largest score change 2014 → 2015 ---
    q_score_change = """
    SELECT u2015.institution, (u2015.score - u2014.score) AS score_change
    FROM university_rankings u2015
    JOIN university_rankings u2014
      ON u2015.institution = u2014.institution
      AND u2015.year = 2015
      AND u2014.year = 2014
    ORDER BY score_change DESC
    LIMIT 10;
    """
    df_score_change = run_query(q_score_change)
    print(df_score_change)

    # Horizontal bar chart with color gradient
    fig3 = px.bar(
        df_score_change,
        y="institution",
        x="score_change",
        orientation="h",
        color="score_change",
        color_continuous_scale="Plasma",
        text="score_change",
        title="Top 10 Universities by Score Change (2014 → 2015)",
    )
    fig3.update_layout(
        xaxis_title="Score Change",
        yaxis_title="University",
        yaxis={"categoryorder": "total ascending"},
    )
    fig3.write_html("score_change_2014_2015_pretty.html")

    print("\nEnhanced visualizations saved as HTML files.")
