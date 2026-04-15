import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from feature_extraction import extract_features

# Load dataset
df = pd.read_csv("dataset/phishing.csv")

# Extract features
X = df['url'].apply(extract_features).tolist()
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")
