from loaddata import load_corpus
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

#  Load data
df = load_corpus()
print(df.head())

X_raw = df['keywords']
y_raw = df['label']

#  Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_raw)

#  Encode labels
le = LabelEncoder()
y = le.fit_transform(y_raw)

#  Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#  Train Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

#  Evaluate
y_pred = model.predict(X_test)
print("\n Classification Report:\n")
print(classification_report(y_test, y_pred))
print(f" Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# #  Save the model & vectorizer
# joblib.dump(model, "model_nb.joblib")
# joblib.dump(vectorizer, "vectorizer.joblib")
# joblib.dump(le, "label_encoder.joblib")

# print("\n Model, vectorizer, and encoder saved!")
