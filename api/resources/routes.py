from resources.authentication import Login, SignUp, Logout, ActivateAccount, NotActivated, ResendActivation
from resources.view import Home
from resources.user import ChangePassword, DeleteUser
from resources.admin import AdminLogin, AdminLogout, ResetUserPassword, SearchUser, ActivateUser, BlockUser, UnblockedUser, AdminDeleteUser, AdminListUsers
from resources.survey import AddSurvey, ListSurveysByUser

def initialize_routes(api):
    api.add_resource(Home, '/api/home')

    api.add_resource(Login, '/api/authentication/login')
    api.add_resource(SignUp, '/api/authentication/signup')
    api.add_resource(Logout, '/api/authentication/logout')
    api.add_resource(ActivateAccount, '/api/authentication/activate/<string:token>')
    api.add_resource(NotActivated, '/api/authentication/notactivated')
    api.add_resource(ResendActivation, '/api/authentication/resend')

    api.add_resource(ChangePassword, '/api/user/changepassword')
    api.add_resource(DeleteUser, '/api/user/delete')
    api.add_resource(ListSurveysByUser, '/api/user/surveys')

    api.add_resource(AdminLogin, '/api/admin/login')
    api.add_resource(AdminLogout, '/api/admin/logout')
    api.add_resource(ResetUserPassword, '/api/admin/resetuserpassword')
    api.add_resource(SearchUser, '/api/admin/searchuser')
    api.add_resource(ActivateUser, '/api/admin/activateuser')
    api.add_resource(BlockUser, '/api/admin/blockuser')
    api.add_resource(UnblockedUser, '/api/admin/unblockeduser')
    api.add_resource(AdminDeleteUser, '/api/admin/deleteuser')
    api.add_resource(AdminListUsers, '/api/admin/listusers')

    api.add_resource(AddSurvey, '/api/survey/add')
    