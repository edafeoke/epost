from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_pyfile('config.py')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/epost'
db = SQLAlchemy(app=app)
mail = Mail(app)
login_manager = LoginManager(app)

# Define your User model in py and import it here
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password, full_name):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.full_name = full_name

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', backref=db.backref('emails', lazy=True))

    def __init__(self, subject, body, user):
        self.subject = subject
        self.body = body
        self.user = user



with app.app_context():
    # db.create_all()
    pass

# Configure Flask-Login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    # Implement the user loader function based on your User model
    return User.query.get(int(user_id))

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
        for i in request.form.items():
            print(i)
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
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            # flash('Login successful.')
            return redirect(url_for('inbox'))
        else:
            flash('Email or Password is incorrect!', category='danger')
            # return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['name']

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please login.', category='danger')
            return redirect(url_for('login'))

        # Create a new user
        new_user = User(email=email, password=password, full_name=full_name)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', category='success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout successful!", category='success')
    return redirect(url_for('login'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
