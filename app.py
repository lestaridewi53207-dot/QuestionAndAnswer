from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------
# MASUKKAN DATA QUIZ-MU DI SINI
# ---------------------------
questions = [
    {
        "question": "Ibukota Indonesia adalah?",
        "choices": ["Bandung", "Jakarta", "Surabaya"],
        "answer": "Jakarta"
    },
    {
        "question": "Python termasuk bahasa…",
        "choices": ["Interpret", "Compiler", "Asembler"],
        "answer": "Interpret"
    }
]
# ---------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = 0

    if request.method == "POST":
        for i, q in enumerate(questions):
            user_ans = request.form.get(f"q{i}")
            if user_ans == q["answer"]:
                score += 1
        return render_template("quiz.html", questions=questions, score=score, done=True)

    return render_template("quiz.html", questions=questions, done=False)


if __name__ == "__main__":
    app.run(debug=True)
