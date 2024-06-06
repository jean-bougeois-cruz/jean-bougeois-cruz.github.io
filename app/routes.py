from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/resume/')
def resume():
    return render_template('resume.html', title='Resume')