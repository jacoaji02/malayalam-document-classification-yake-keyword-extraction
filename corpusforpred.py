import requests
from bs4 import BeautifulSoup
import re
import yake

def clean_malayalam_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator=' ')
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[0-9]', '', text)
    text = re.sub(r'[^\u0D00-\u0D7F\s,.!?]', '', text)
    return text


urls = [
    "https://malayalammedia.live/2025/06/14/14-22-crores-lapsed-sunny-joseph-tells-the-truth-through-saseendran-ldf-hides-saseendran-from-nilambur-hilly-areas/"

]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    paragraphs = soup.find_all("p")
    raw_text = "\n".join([p.get_text().strip() for p in paragraphs]).strip()
    cleaned_text = clean_malayalam_html(raw_text)

with open("pred2.txt", "w", encoding= "utf-8") as file:
    file.write(cleaned_text)

