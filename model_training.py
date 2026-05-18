import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle

# Load dataset
df = pd.read_csv("fake_job_postings.csv")

# Fill missing values
df.fillna('', inplace=True)

# Combine text columns
df['text'] = (
    df['title'] + ' ' +
    df['description'] + ' ' +
    df['company_profile']
)

# Features and labels
X = df['text']
y = df['fraudulent']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english')

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()

model.fit(X_train_vectorized, y_train)

# Predictions
predictions = model.predict(X_test_vectorized)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("Model Saved Successfully")