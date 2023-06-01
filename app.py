from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Sample inbox data
inbox = [
    { 'from': 'sender1@example.com', 'subject': 'Sample Email 1' },
    { 'from': 'sender2@example.com', 'subject': 'Sample Email 2' },
    { 'from': 'sender3@example.com', 'subject': 'Sample Email 3' }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inbox', methods=['GET'])
def get_inbox():
    return jsonify(inbox)

@app.route('/compose', methods=['POST'])
def compose_email():
    to = request.form['to']
    subject = request.form['subject']
    message = request.form['message']

    # Send email logic goes here...

    # For demonstration purposes, just append the composed email to the inbox
    inbox.append({ 'from': to, 'subject': subject })

    return jsonify({ 'message': 'Email sent successfully!' })

if __name__ == '__main__':
    app.run(debug=True)
