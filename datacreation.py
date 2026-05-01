import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
import yake
import time


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='####',
    database='keywordextraction',
    charset='utf8mb4'
)
cursor = conn.cursor()


def clean_malayalam_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator=' ')
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\u0D00-\u0D7F\s,.!?]', '', text)
    return text


kw_extractor = yake.KeywordExtractor(lan="ml", n=2, top=5)

def extract_keywords(clean_text):
    keywords = kw_extractor.extract_keywords(clean_text)
    return ', '.join([kw for kw, score in keywords])


urls = [
    ("https://www.mathrubhumi.com/news/kerala/cpi-mla-cc-mukundan-thrissur-district-council-exclusion-1.10746213", "politics"),
    ("https://www.mathrubhumi.com/news/kerala/amit-shah-bjp-kerala-future-1.10741007", "politics"),
    ("https://www.mathrubhumi.com/sports/cricket/nitish-kumar-reddy-injured-out-of-england-series-1.10765860", "sports"),
    ("https://www.mathrubhumi.com/sports/cricket/bangladesh-vs-pakistan-1st-t20-pitch-controversy-1.10765664", "sports")
]

for full_url, label in urls:
    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, "html.parser")   

    paragraphs = soup.find_all("p")
    raw_text = "\n".join([p.get_text().strip() for p in paragraphs]).strip()

    cleaned_text = clean_malayalam_html(raw_text)
    if len(cleaned_text) < 50:
        print(f" Skipping (too short): {full_url}")
        continue

    
    cursor.execute("SELECT COUNT(*) FROM malayalam_corpus WHERE source_url = %s", (full_url,))
    if cursor.fetchone()[0] > 0:
        print(f" Already exists, skipped: {full_url}")
        continue

    
    keyword_text = extract_keywords(cleaned_text)

    
    sql = """
        INSERT INTO malayalam_corpus (text, label, source_url, keywords)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (cleaned_text, label, full_url, keyword_text))
        conn.commit()
        print(f" Added: {full_url} | Keywords: {keyword_text}")
    except mysql.connector.IntegrityError:
        print(f" Duplicate URL blocked by UNIQUE: {full_url}")

    time.sleep(1)

cursor.close()
conn.close()
