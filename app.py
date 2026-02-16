from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", theme="welcome")

@app.route("/hello")
def hello():
    return render_template("hello.html", theme="hello")

@app.route("/soul")
def soul():
    return render_template("soul.html", theme="soul")


if __name__ == "__main__":
    app.run(debug=True)
