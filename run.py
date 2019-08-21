from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('layout.html')

@app.route("/fr.html")
def home_fr():
    return render_template('layoutfr.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)