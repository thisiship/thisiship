from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tonisbones'}
    posts = [
        {
            'author': {'username': 'tonisbones'},
            'body': 'thisiship is hip!'
        },
        {
            'author': {'username': 'tone'},
            'body': 'thisiship is too hip!'
        }
    ]
            
    return render_template('index.html', title='Home', user=user, posts=posts)
