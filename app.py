from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake data to simulate predictions and bets
user_bets = []
trending_predictions = [
    {"coin": "DogeCoin", "prediction": "100x by next month", "pool": "Live"},
    {"coin": "Pepe", "prediction": "$1 before 2026", "pool": "Filling"},
    {"coin": "SHIBA", "prediction": "New all-time high", "pool": "Closed"},
]

@app.route('/')
def home():
    return render_template('index.html', trending=trending_predictions)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        coin = request.form['coin']
        prediction = request.form['prediction']
        exit_point = request.form.get('exit')
        user_bets.append({
            "coin": coin,
            "prediction": prediction,
            "exit": exit_point,
            "status": "Pending"
        })
        return redirect(url_for('my_bets'))
    return render_template('predict.html')

@app.route('/dashboard')
def dashboard():
    win_rate = "80%"  # placeholder
    total_predictions = len(user_bets)
    return render_template('dashboard.html', total=total_predictions, win_rate=win_rate)

@app.route('/bets')
def my_bets():
    return render_template('bets.html', bets=user_bets)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Simulate saving changes
        return redirect(url_for('dashboard'))
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
