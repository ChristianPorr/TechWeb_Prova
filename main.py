from flask import Flask, redirect, render_template, url_for, request, session
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/newcard")
def card():
    return render_template("newcard.html")



if __name__ == '__main__':
    app.run(debug=True)
