from flask import render_template
from random import choice
from app import app


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    greetings = ['You seem to have taken a wrong turn...',
        'Orcs attack, roll initiative',
        'Speak friend and enter']
    return render_template('index.html', text=choice(greetings))

