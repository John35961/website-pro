from flask import Flask, render_template, redirect
import yaml

app = Flask(__name__)

@app.route("/")
def home():
    return redirect('en')

@app.route("/en/")
def en():
    with open('content/home/en-home.yml', 'r') as file:
        yml = yaml.safe_load(file)

    with open('content/projects.yml', 'r') as file:
        proj = yaml.safe_load(file)

    return render_template('EN_layout.html', yml=yml, proj=proj)

@app.route("/fr/")
def fr():
    with open('content/home/fr-home.yml', 'r') as file:
        yml = yaml.safe_load(file)

    return render_template('FR_layout.html', yml=yml)

if __name__ == "__main__":
    app.run(debug=True)
