from app import app
from flask import render_template
from app.forms import RegisterForm

@app.route('/')
def index():
    name = 'Ankit'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('THE FORM IS VALID!!!!')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        
    return render_template('register.html', title='Register for CT Blog', form=form)