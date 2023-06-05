from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
mail = Mail(app)

# Define your models in models.py and import them here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox', methods=['POST'])
def inbox():
    return render_template('inbox.html')

@app.route('/compose', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
