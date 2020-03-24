from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect('en')

@app.route("/en/")
def en():
    return render_template('EN_layout.html')

@app.route("/fr/")
def fr():
    return render_template('FR_layout.html')

if __name__ == "__main__":
    app.run(debug=True)