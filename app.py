from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'emails.db'

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_email_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            recipient TEXT NOT NULL,
            subject TEXT NOT NULL,
            body TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'unread',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    emails = conn.execute('SELECT * FROM emails').fetchall()
    conn.close()
    return render_template('index.html', emails=emails)

@app.route('/compose', methods=['GET', 'POST'])
def compose():
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']

        conn = get_db_connection()
        conn.execute('INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)',
                     (sender, recipient, subject, body))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Email sent successfully.'})
    
    return render_template('compose.html')

@app.route('/email/<int:email_id>')
def email(email_id):
    conn = get_db_connection()
    email = conn.execute('SELECT * FROM emails WHERE id = ?', (email_id,)).fetchone()
    conn.close()
    return render_template('email.html', email=email)

@app.route('/delete/<int:email_id>', methods=['POST'])
def delete(email_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM emails WHERE id = ?', (email_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Email deleted successfully.'})

if __name__ == '__main__':
    create_email_table()
    app.run(debug=True)
