import mysql.connector
import pandas as pd

def load_corpus():


    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='####',
        database='keywordextraction',
        charset='utf8mb4'
    )


    query = "SELECT keywords, label FROM malayalam_corpus"
    df = pd.read_sql(query, conn)

    conn.close()

    return df

if __name__ == "__main__":
    df = load_corpus()
    print(df.head())
    print("\nClass counts:")
    print(df['label'].value_counts())
