📌 Malayalam Keyword Extraction & Text Classification using YAKE 

🧠 Overview

This project focuses on automatic keyword extraction from Malayalam text documents using the YAKE! (Yet Another Keyword Extractor) and utilizes the extracted keywords for text classification.

The system is designed as an unsupervised + supervised pipeline, where:

Keywords are extracted using YAKE (unsupervised)
Extracted keywords are used to train a classifier (supervised)

This work contributes to Natural Language Processing (NLP) research in low-resource languages like Malayalam, addressing challenges due to its morphologically rich and agglutinative nature.

🎯 Objectives

1) Develop a keyword extraction system for Malayalam text

2) Use YAKE for language-independent keyword extraction

3) Build a structured corpus using MySQL

4) Train a machine learning model for text classification

5) Enable automatic prediction of document categories

⚙️ System Architecture

🔹 1. Data Collection

Malayalam news articles are collected via web scraping
Sources include multiple online news platforms
Categories used:
Politics
Sports

🔹 2. Database Design

Data is stored in a MySQL database with the following schema:

id	(Unique identifier)

text	(Cleaned Malayalam text)

label	(Name of the category sports/politics)

source_url	(Article URL)

date_scraped	(Timestamp)

keywords	(Extracted keywords)

🔹 3. Preprocessing

HTML parsing using BeautifulSoup
Removal of:

  Non-Malayalam characters
  
  Extra whitespace
  
  Retains only Malayalam Unicode range:
\u0D00 – \u0D7F

🔹 4. Keyword Extraction (YAKE)

The YAKE algorithm extracts keywords based on statistical features such as:

Word frequency

Position in text

Context relevance

Casing and sentence distribution

Key characteristics:

❌ No training required
🌐 Language-independent
⚡ Works on single documents

Output:

Top 5 keywords per document

🔹 5. Data Pipeline
Scrape article
     ↓ 
Clean text
     ↓ 
Extract keywords using YAKE
     ↓ 
Store results in MySQL


🔹 6. Model Training

📌 Data Preparation
Keywords and labels are loaded into Pandas DataFrame
Features:

Input → keywords

Output → category label

📌 Feature Extraction

Text is converted using:
TF-IDF Vectorization

📌 Model Used

Multinomial Naive Bayes

⚠️ Dataset Note

The dataset consists of Malayalam news articles collected from online sources.

Due to licensing and copyright constraints, the full dataset is not included in this repository.

📊 Applications

Text Classification,
Information Retrieval,
Document Summarization,
Malayalam NLP Research

🔮 Future Work

Increase dataset size and categories,
Improve classification performance,
Integrate deep learning models,
Extend to other Indian languages
