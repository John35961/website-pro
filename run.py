from flask import Flask, render_template, redirect
import yaml

app = Flask(__name__)

@app.route("/")
def home():
    return redirect('en')

@app.route("/en/")
def en():
    return render_template('EN_layout.html')

@app.route("/fr/")
def fr():
    with open('content/fr.yml', 'r') as file:
        yml = yaml.safe_load(file)

    return render_template('FR_layout.html', yml=yml)

if __name__ == "__main__":
    app.run(debug=True)
