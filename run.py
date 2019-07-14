from flask import Flask
from flask_simpleldap import LDAP

app = Flask(__name__)
app.config['LDAP_BASE_DN'] = 'OU=users,dc=example,dc=org'
app.config['LDAP_USERNAME'] = 'CN=user,OU=Users,DC=example,DC=org'
app.config['LDAP_PASSWORD'] = 'password'

ldap = LDAP(app)


@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'


if __name__ == '__main__':
    app.run()

