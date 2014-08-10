Flask-SimpleLDAP
================

Flask-SimpleLDAP provides LDAP authentication for Flask.

Quickstart
-------

    from flask import Flask
    from flask.ext.simpleldap import LDAP

    app = Flask(__name__)
    ldap = LDAP(app)

    app.config['LDAP_BASE_DN'] = 'OU=users,dc=example,dc=org'
    app.config['LDAP_USERNAME'] = 'CN=user,OU=Users,DC=example,DC=org'
    app.config['LDAP_PASSWORD'] = 'password'


Resources
---------

- [Documentation](http://flask-simpleldap.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SimpleLDAP)
