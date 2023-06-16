# Flask configuration
SECRET_KEY = 'your-secret-key'
# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/epost'
SQLALCHEMY_DATABASE_URI = 'sqlite:///epost.db'

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'greatedafeoke@gmail.com'
MAIL_PASSWORD = 'sdzimhvcqzrbenzc'
MAIL_DEFAULT_SENDER = 'greatedafeoke@gmail.com'
