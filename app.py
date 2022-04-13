from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hobbies')
def hobbies():
    return render_template("hobbies.html")

@app.route('/work-experience')
def jobs():
    return render_template("jobs.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/extracurriculars')
def clubs():
    return render_template("clubs.html")

@app.route('/personal-projects')
def projects():
    return render_template("projects.html")