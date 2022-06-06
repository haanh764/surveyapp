from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from app import app, mail

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['JWT_SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['JWT_SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

def send_email(to, subject, confirm_url):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = 'Your confirmation link is here: {}'.format(confirm_url)
    mail.send(msg)
