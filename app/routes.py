from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, CreatePostForm
from app.models import User, Post

@app.route('/')
def index():
    name = 'Ankit'
    title = "Ankit's Blog"
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Grab data from our submitted form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)
        

    

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        # Once new_user is added to db, flash success message
        flash(f'Thank you for signing up {new_user.username}!', 'info')

        # Redirect user back to home page
        return redirect(url_for('index'))
    
           
    return render_template('register.html', title='Register for CT Blog', form=form)


@app.route('/createpost', methods= ['GET', 'POST'])
def createpost():
    form = CreatePostForm()
    if form.validate_on_submit():
        #Grab data from form
        title = form.title.data
        body = form.body.data
        print(title,body)
        #Create new instance of Post from form database
        new_post = Post(title, body, 1)
        
        #Add new_post to database
        db.session.add(new_post)
        db.session.commit()
        
        #Flash Message for post 
        flash(f'Your post has been created successfully {new_post.author.username}!', 'success')
        
        # Redirect user back to home page
        return redirect(url_for('index'))
        
    return render_template('createpost.html', form=form)