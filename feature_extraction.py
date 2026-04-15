import re
from urllib.parse import urlparse

def extract_features(url):
    features = []

    # Length of URL
    features.append(len(url))

    # Check for HTTPS
    features.append(1 if "https" in url else 0)

    # Count dots
    features.append(url.count("."))

    # Presence of @ symbol
    features.append(1 if "@" in url else 0)

    # Presence of - symbol
    features.append(1 if "-" in url else 0)

    # Count digits
    features.append(sum(c.isdigit() for c in url))

    # Suspicious words
    suspicious_words = ['login', 'verify', 'update', 'secure', 'account', 'bank']
    features.append(sum(word in url.lower() for word in suspicious_words))

    return features
