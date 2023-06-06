from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, login_user, login_required, logout_user
import models

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager(app)

# Define your User model in models.py and import it here

# Configure Flask-Login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Implement the user loader function based on your User model
    return models.User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox', methods=['POST', 'GET'])
@login_required
def inbox():
    # Handle inbox route for authenticated users only
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

# Add your routes for registration, login, and other functionality
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Validate the login credentials and login the user
        user = models.User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})
        else:
            return jsonify({'message': 'Invalid email or password'})
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print("inside the post method")
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['name']

        # Check if the user already exists
        user = models.User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login.')
            return redirect(url_for('login'))

        # Create a new user
        new_user = models.User(email=email, password=password, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.')
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
