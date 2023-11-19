from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    return render_template('story.html', text=story.generate(request.args))