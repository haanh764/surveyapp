from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from app import app, mail, jwt
from common.settings import MAIL_USERNAME
from flask_jwt_extended import get_jwt, verify_jwt_in_request
import random
import string

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

def admin_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            print(claims)
            if claims['is_admin']:
                return fn(*args, **kwargs)
            else:
                return {'message': 'Admin only! You are not authorized to perform this action!'}, 403
        return wrapper
    return decorator

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    combine = lower + upper + num
    password = "".join(random.sample(combine, length))
    return password
    