from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
def index():
    user = {'username': 'Renee'}
    posts= [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movies was so cool!'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)