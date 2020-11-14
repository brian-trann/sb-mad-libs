from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    '''Return Homepage '''
    story_prompts = story.prompts
    return render_template('index.html', story_prompts=story_prompts)

@app.route('/story')
def story_route():
    '''render Story page. create a story instance'''
    answers = request.args
    user_story = story.generate(answers)
    return render_template('story.html', user_story=user_story)

    