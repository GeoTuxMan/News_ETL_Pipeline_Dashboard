import sqlite3
import pandas as pd

DB_PATH = "news.db"
TABLE_NAME = "articles"

def save_to_db(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
