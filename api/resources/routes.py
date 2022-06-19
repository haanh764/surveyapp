from resources.authentication import Login, SignUp, Logout, ActivateAccount, NotActivated, ResendActivation
from resources.view import Home
from resources.user import ChangePassword, DeleteUser, isBlocked, UserDeleteSurvey
from resources.admin import AdminLogin, AdminLogout, ResetUserPassword, SearchUser, ActivateUser, BlockUser, UnblockedUser, AdminDeleteUser, AdminListUsers, AdminDeleteSurvey, AdminChangePassword, AdminListSurveys
from resources.survey import AddSurvey, ListSurveysByUser, GetSurvey
from resources.response import AddResponse
from resources.analysis_datatable import GenrateDataTable
from resources.analysis_dashboard import GetDataSummary

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
    api.add_resource(isBlocked, '/api/user/isblocked')
    api.add_resource(UserDeleteSurvey, '/api/user/survey/delete')

    api.add_resource(AdminLogin, '/api/admin/login')
    api.add_resource(AdminLogout, '/api/admin/logout')
    api.add_resource(ResetUserPassword, '/api/admin/resetuserpassword')
    api.add_resource(SearchUser, '/api/admin/searchuser')
    api.add_resource(ActivateUser, '/api/admin/activateuser')
    api.add_resource(BlockUser, '/api/admin/blockuser')
    api.add_resource(UnblockedUser, '/api/admin/unblockeduser')
    api.add_resource(AdminDeleteUser, '/api/admin/deleteuser')
    api.add_resource(AdminListUsers, '/api/admin/listusers')
    api.add_resource(AdminDeleteSurvey, '/api/admin/deletesurvey')
    api.add_resource(AdminChangePassword, '/api/admin/changepassword')
    api.add_resource(AdminListSurveys, '/api/admin/listsurveys')

    api.add_resource(AddSurvey, '/api/survey/add')
    api.add_resource(GetSurvey, '/api/survey/get/<string:survey_id>')
    api.add_resource(GenrateDataTable, '/api/analysis/generatedatatable/<string:survey_id>')
    api.add_resource(GetDataSummary, '/api/analysis/getsummary/<string:survey_id>')
    api.add_resource(AddResponse, '/api/respond/<string:survey_id>')
