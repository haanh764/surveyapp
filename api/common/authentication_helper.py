from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from app import app, mail, jwt
from common.settings import MAIL_USERNAME
from flask_jwt_extended import get_jwt, verify_jwt_in_request

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

# def validate_admin_email(email):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#             if email == MAIL_USERNAME:
#                 return fn(*args, **kwargs)
#             else:
#                 return {'message': 'You are not authorized to perform this action!'}, 403

def admin_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            if get_jwt()['email'] == MAIL_USERNAME:
                return fn(*args, **kwargs)
            else:
                return {'message': 'You are not authorized to perform this action!'}, 403
        return wrapper
    return decorator
