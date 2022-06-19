DB_URL = "mysql+pymysql://user:password123@db/surveydb"
JWT_SECRET_KEY = 'flflGgXwUkT75bBPjxc7qQ'
SECURITY_PASSWORD_SALT = 'surveyapp1234567890'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_USERNAME = 'surveyapp.manager@gmail.com'
MAIL_PASSWORD = 'jijummhpverqwtjk'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
ADMIN_PSWD = 'admin123'
PROPAGATE_EXCEPTIONS = True
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
JWT_COOKIE_SECURE = False
JWT_TOKEN_LOCATION = ['headers']
JWT_COOKIE_CSRF_PROTECT = False
JWT_HEADER_NAME = 'Authorization'
JWT_HEADER_TYPE = ''