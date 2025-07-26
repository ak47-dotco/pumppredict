# PumpPredict Full Flask Web App Code
# Includes routes, templates, and setup files (HTML not included in this cell)

from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Mock prediction data
predictions = [
    {
        "id": 1,
        "coin": "DOGE",
        "title": "DOGE to hit $0.30 in 24h",
        "type": "24h",
        "status": "live",
        "end_time": datetime.datetime.now() + datetime.timedelta(hours=24),
        "bets": []
    },
    {
        "id": 2,
        "coin": "PEPE",
        "title": "PEPE to double this week",
        "type": "weekly",
        "status": "intermediate",
        "end_time": datetime.datetime.now() + datetime.timedelta(days=7),
        "bets": []
    }
]

user_bets = []

@app.route("/")
def home():
    return render_template("index.html", predictions=predictions)

@app.route("/predict/<int:pred_id>", methods=["GET", "POST"])
def predict(pred_id):
    prediction = next((p for p in predictions if p['id'] == pred_id), None)
    if not prediction:
        return "Prediction not found", 404

    if request.method == "POST":
        username = request.form.get("username")
        prediction_text = request.form.get("prediction")
        exit_point = request.form.get("exit_point")
        amount = request.form.get("amount")

        bet = {
            "username": username,
            "prediction": prediction_text,
            "exit_point": exit_point,
            "amount": amount,
            "time": datetime.datetime.now()
        }
        prediction['bets'].append(bet)
        user_bets.append(bet)
        return redirect(url_for("home"))

    return render_template("predict.html", prediction=prediction)

@app.route("/account")
def account():
    return render_template("account.html", user_bets=user_bets)

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)

