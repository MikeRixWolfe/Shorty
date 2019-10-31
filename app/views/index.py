from flask import render_template
from app import app


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    return render_template('index.html')

