from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, CreatePostForm, LoginForm
from app.models import User, Post
from flask_login import login_required, login_user, logout_user


@app.route('/')
def index():
    name = 'Ankit'
    title = "Ankit's Blog"
    all_posts = Post.query.all()
    return render_template('index.html', name=name, title=title, posts=all_posts)

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
@login_required
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

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
                
        if user is None or not user.check_password(password):
            flash('Incorrect Username/Password. Please try again!', 'danger')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('You have successfully logged in!', 'success')
        return redirect(url_for('index'))
            
        
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))
