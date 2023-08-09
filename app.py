from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    prompts = story.prompts

    return render_template('main.html', prompts=prompts)


@app.route('/story')
def your_story():
    
    the_story = story.generate(request.args)
    return render_template('the_story.html', the_story=the_story)