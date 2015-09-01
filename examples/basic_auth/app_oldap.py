from flask import Flask, g, request, session, redirect, url_for
from flask.ext.simpleldap import LDAP

app = Flask(__name__)
app.secret_key = 'dev key'
app.debug = True

app.config['LDAP_OPENLDAP'] = True
app.config['LDAP_OBJECTS_DN'] = 'dn'
app.config['LDAP_REALM_NAME'] = 'OpenLDAP Authentication'
app.config['LDAP_HOST'] = 'openldap.example.org'
app.config['LDAP_BASE_DN'] = 'dc=users,dc=openldap,dc=org'
app.config['LDAP_USERNAME'] = 'cn=user,ou=servauth-users,dc=users,dc=openldap,dc=org'
app.config['LDAP_PASSWORD'] = 'password'
app.config['LDAP_USER_OBJECT_FILTER'] = '(&(objectclass=inetOrgPerson)(uid=%s))'

ldap = LDAP(app)

@app.route('/')
@ldap.basic_auth_required
def index():
    return 'Welcome, {0}!'.format(g.ldap_username)

if __name__ == '__main__':
    app.run()
