from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm
from app.models import User
from app.models import Post



@app.route('/')
def index():
    name = 'Ankit'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #Grab data from the submitted form
        print('THE FORM IS VALID!!!!')
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)
        
        #Add new__user to the database
        db.session.add(new_user)
        db.session.commit()
        
        # Once new_user is added to db, flash success messages
        flash(f'Thank you for registering {new_user.username}!', 'primary')
        
        #Redirect user back to home page
        return redirect(url_for('index'))
        
    return render_template('register.html', title='Register for CT Blog', form=form)