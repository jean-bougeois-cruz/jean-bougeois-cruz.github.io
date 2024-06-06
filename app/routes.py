from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    print("Home route accessed")
    return render_template('index.html', title='Home')

@app.route('/resume/')
def resume():
    return render_template('resume.html', title='Resume')