from flask import Flask, request, render_template_string
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

# Load model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Phishing URL Detector</title>
</head>
<body>
    <h2>🔍 Phishing URL Detector</h2>
    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL" required>
        <button type="submit">Check</button>
    </form>
    {% if result %}
        <h3>{{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        features = [extract_features(url)]
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "⚠️ Phishing URL Detected!"
        else:
            result = "✅ Safe URL"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
