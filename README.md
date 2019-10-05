Flask-SimpleLDAP
================

[![Build Status](https://travis-ci.org/admiralobvious/flask-simpleldap.svg?branch=master)](https://travis-ci.org/admiralobvious/flask-simpleldap)

Flask-SimpleLDAP provides LDAP authentication for Flask.

Flask-SimpleLDAP is compatible with and tested on Python 3.5, 3.6 and 3.7.

Quickstart
----------

First, install Flask-SimpleLDAP:
    
    $ pip install flask-simpleldap
    
Flask-SimpleLDAP depends, and will install for you, recent versions of Flask
(0.12.4 or later) and [python-ldap](https://python-ldap.org/).
Please consult the [python-ldap installation instructions](https://www.python-ldap.org/en/latest/installing.html) if you get an error during installation.

Next, add a ``LDAP`` instance to your code and at least the three
required configuration options:

```python
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

```

You can take a look at [examples/groups](examples/groups) for a more complete 
example using LDAP groups.

You can also take a look at [examples/blueprints](examples/blueprints) for an 
example using Flask's 
[application factories](http://flask.pocoo.org/docs/patterns/appfactories/) 
and [blueprints](http://flask.pocoo.org/docs/blueprints/).


OpenLDAP
--------

Add the ``LDAP`` instance to your code and depending on your OpenLDAP
configuration, add the following at least LDAP_USER_OBJECT_FILTER and 
LDAP_USER_OBJECT_FILTER.

```python
from flask import Flask
from flask_simpleldap import LDAP

app = Flask(__name__)

# Base
app.config['LDAP_REALM_NAME'] = 'OpenLDAP Authentication'
app.config['LDAP_HOST'] = 'openldap.example.org'
app.config['LDAP_BASE_DN'] = 'dc=users,dc=openldap,dc=org'
app.config['LDAP_USERNAME'] = 'cn=user,ou=servauth-users,dc=users,dc=openldap,dc=org'
app.config['LDAP_PASSWORD'] = 'password'

# OpenLDAP 
app.config['LDAP_OBJECTS_DN'] = 'dn'
app.config['LDAP_OPENLDAP'] = True
app.config['LDAP_USER_OBJECT_FILTER'] = '(&(objectclass=inetOrgPerson)(uid=%s))'

# Groups
app.config['LDAP_GROUP_MEMBERS_FIELD'] = "uniquemember"
app.config['LDAP_GROUP_OBJECT_FILTER'] = "(&(objectclass=groupOfUniqueNames)(cn=%s))"
app.config['LDAP_GROUP_MEMBER_FILTER'] = "(&(cn=*)(objectclass=groupOfUniqueNames)(uniquemember=%s))"
app.config['LDAP_GROUP_MEMBER_FILTER_FIELD'] = "cn"

ldap = LDAP(app)


@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'


if __name__ == '__main__':
    app.run()

```

Resources
---------

- [Documentation](http://flask-simpleldap.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SimpleLDAP)
