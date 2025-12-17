from flask import Flask, render_template, request, session
import pickle

app = Flask(__name__)
app.secret_key = "spam-secret-key"

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        message = request.form["message"]
        data = vectorizer.transform([message])
        result = model.predict(data)

        prediction = "🚫 Spam Message" if result[0] == 1 else "✅ Not Spam"

        session["history"].insert(0, {
            "text": message[:50] + ("..." if len(message) > 50 else ""),
            "result": prediction
        })

        session["history"] = session["history"][:5]

    return render_template(
        "index.html",
        prediction=prediction,
        history=session["history"]
    )

if __name__ == "__main__":
    app.run(debug=True)
