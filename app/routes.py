from flask import Blueprint, render_template, request, jsonify

from app import db
from app.models import Email

bp = Blueprint('email', __name__)

@bp.route('/', methods=['GET'])
def index():
    emails = Email.query.order_by(Email.timestamp.desc()).all()
    return render_template('index.html', emails=emails)

@bp.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        email = Email(sender=sender, recipient=recipient, subject=subject, body=body)
        db.session.add(email)
        db.session.commit()

        return jsonify({'message': 'Email sent successfully'})

    return render_template('compose.html')

@bp.route('/email/<int:email_id>', methods=['GET'])
def email(email_id):
    email = Email.query.get_or_404(email_id)
    return render_template('email.html', email=email)

@bp.route('/emails', methods=['GET'])
def emails():
    emails = Email.query.order_by(Email.timestamp.desc()).all()
    return render_template('emails.html', emails=emails)
