from flask import Blueprint, g, request, session, redirect, url_for
from ..extensions import ldap

core = Blueprint('core', __name__)


@core.route('/')
@ldap.login_required
def index():
    return 'Successfully logged in!'


@core.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = request.form['user']
        passwd = request.form['passwd']
        test = ldap.bind_user(user, passwd)
        if test is None:
            return 'Invalid credentials'
        else:
            session['user_id'] = request.form['user']
            return redirect('/')
    return """<form action="" method="post">
                user: <input name="user"><br>
                password:<input type="password" name="passwd"><br>
                <input type="submit" value="Submit"></form>"""


@core.route('/group')
@ldap.group_required(groups=['Web Developers', 'QA'])
def group():
    return 'Group restricted page'


@core.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))
