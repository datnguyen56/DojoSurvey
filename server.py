from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("survey.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html",
    your_name = request.form['your_name'],
    dojo_location = request.form['dojo_location'],
    favorite_language = request.form['favorite_language'],
    comment = request.form['comment'])

if __name__ == "__main__":
    app.run(debug=True)