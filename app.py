from flask import Flask, render_template, request
questions = {}

app = Flask(__name__)
@app.route("/")
def home_page():
    test = "а это информация из бэка"
    return render_template("index.html", back=test)

@app.route("/user/<int:pk>/video/<string:name>")
def user_info(pk, name):
    return f"информация видео {name} юзера {pk}"

@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        title = request.form.get("title")
        main_text = request.form.get("main_text")
        questions[title] = main_text
        if title and main_text:
            questions[title] = {'text': main_text, 'answers': []}
        return render_template("question.html", questions=questions)
    elif request.method == "GET":
        return "так по ссылке переходить нельзя"

@app.route("/answer-question/<title>", methods=["POST"])
def answer_question(title):
    answer = request.form.get("answer")
    if answer and title in questions:
        questions[title]['answers'].append(answer)
    return render_template("question.html", questions=questions)

app.run(debug=True)