
import joblib
import yake

#   Load your trained pieces
model = joblib.load("model_nb.joblib")
vectorizer = joblib.load("vectorizer.joblib")
le = joblib.load("label_encoder.joblib")

# Load text from cleaned .txt file
with open("pred2.txt", "r", encoding="utf-8") as f:
    new_article_text = f.read().strip()

print(" Loaded article text from file.")

#   Extract keywords with YAKE (same settings as training)
kw_extractor = yake.KeywordExtractor(lan="ml", n=2, top=5)
keywords_scored = kw_extractor.extract_keywords(new_article_text)

new_keywords = ", ".join([kw for kw, score in keywords_scored])

print(f" Extracted keywords: {new_keywords}")

#  Vectorize & predict
X_new = vectorizer.transform([new_keywords])
y_pred = model.predict(X_new)
predicted_label = le.inverse_transform(y_pred)[0]

print(f" Predicted label: {predicted_label}")

