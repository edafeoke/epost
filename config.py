# Flask configuration
SECRET_KEY = 'your-secret-key'
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/epost'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'greatedafeoke@gmail.com'
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'greatedafeoke@gmail.com'
