from models.admin import Admin
from common.settings import MAIL_USERNAME, ADMIN_PSWD

def init_admin_default():
    admin = Admin(MAIL_USERNAME, ADMIN_PSWD)
    admin.generate_password()
    admin.add_admin()
    