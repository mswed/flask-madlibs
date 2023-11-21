import json
import re
import os
from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)
counter = {}

story = None


@app.route('/')
def home_page():
    stories = None
    if os.path.isfile('stories.json'):
        with open('stories.json', 'r') as input_file:
            stories = json.load(input_file)
    return render_template('home.html', stories=stories)

@app.route('/madlib')
def madlib_maker():
    global story

    if os.path.isfile('stories.json'):
        with open('stories.json', 'r') as input_file:
            stories = json.load(input_file)
    selected_story = stories.get(request.args.get('story'))

    if selected_story:
        story = Story(request.args.get('story'), selected_story['words'], selected_story['text'])
        return render_template('maker.html', prompts=story.prompts)


@app.route('/story')
def show_story():
    global story
    return render_template('story.html', text=story.generate(request.args))


@app.route('/new')
def make_new_story():
    return render_template('new_story.html')


def renumber(match):
    v = match.group(1)
    if v in counter.keys():
        counter[v] += 1
    else:
        counter[v] = 1
    return '{' + match.group(1) + str(counter[v]) + '}'


@app.route('/create')
def create_story():
    story_name = request.args.get('story-name')
    story_text = request.args.get('new-story')
    modified_text = re.sub(r'\{(.*?)\}', renumber, story_text)
    variables = re.findall(r'\{(.*?)\}', modified_text)
    new_story = Story(story_name, variables, modified_text)
    new_story.save()

    return render_template('submitted-story.html', story_name=story_name)

