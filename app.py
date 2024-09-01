from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/work-experience')
def jobs():
    return render_template("jobs.html")

@app.route('/design-teams')
def clubs():
    return render_template("clubs.html")

@app.route('/personal-projects')
def projects():
    return render_template("projects.html")

@app.route('/about-me')
def about():
    return render_template("about.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")