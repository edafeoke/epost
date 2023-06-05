from flask import render_template, redirect, request, url_for, flash, jsonify, Blueprint
from flask_login import login_user, logout_user, login_required
from app import app, db, mail
from models import User
from flask_mail import  Message
from flask_login import login_user, login_required, logout_user

routes = Blueprint('routes', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login.')
            return redirect(url_for('login'))

        # Create a new user
        new_user = User(email=email, password=password, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find the user by email
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful.')
            return redirect(url_for('inbox'))
        else:
            flash('Invalid email or password.')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))

@app.route('/inbox', methods=['GET', 'POST'])
@login_required
def inbox():
    return render_template('inbox.html')

@app.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']
        # Send the email using Flask-Mail
        msg = Message(subject, recipients=[recipient])
        msg.body = body
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'})
    return render_template('compose.html')
