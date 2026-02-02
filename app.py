from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Här har jag uppdaterat texten och lagt till lite enkel styling
    return """
    <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9;">
        <h1 style="color: #4285f4;">Nu har jag fattat det här!</h1>
        <p style="font-size: 1.2em;">Min app uppdateras automatiskt via GitHub Actions.</p>
        <p>Det här körs live på <strong>Google Cloud 2026</strong> 🚀</p>
    </body>
    """

if __name__ == "__main__":
    # Cloud Run sätter miljövariabeln PORT automatiskt
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))