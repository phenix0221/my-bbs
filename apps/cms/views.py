from flask import Blueprint, views, render_template

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return 'cms index'


class LoginView(views.MethodView):

    @staticmethod
    def get():
        return render_template('cms/login.html')

    def post(self):
        pass


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
