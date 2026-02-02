from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Succé!</h1><p>Din Flask-app körs nu på Google Cloud 2026.</p>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
