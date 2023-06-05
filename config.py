# Flask configuration
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/epost'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'greatedafeoke@gmail.com'
MAIL_PASSWORD = 'your-password'
MAIL_DEFAULT_SENDER = 'greatedafeoke@gmail.com'
