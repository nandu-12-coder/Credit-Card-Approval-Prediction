from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("models/credit_card_model.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    income = float(request.form["income"])
    age = float(request.form["age"])
    employment = float(request.form["employment"])

    prediction = model.predict([[income, age, employment]])

    if prediction[0] == 1:
        output = "Credit Card Approved"
    else:
        output = "Credit Card Rejected"

    return render_template(
        "result.html",
        prediction=output
    )


if __name__ == "__main__":
    app.run(debug=True)