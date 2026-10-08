from flask import Flask, render_template, jsonify
import requests


app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/api/traffic"


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/dashboard")
def dashboard_data():
    try:
        response = requests.get(
            BACKEND_URL,
            timeout=5
        )

        response.raise_for_status()

        return jsonify(response.json())

    except requests.exceptions.RequestException as error:
        return jsonify({
            "error": "Unable to connect to traffic backend",
            "details": str(error)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )