Flask-SimpleLDAP
================

[![Build Status](https://travis-ci.org/admiralobvious/flask-simpleldap.png?branch=master)](https://travis-ci.org/admiralobvious/flask-simpleldap)

Flask-SimpleLDAP provides LDAP authentication for Flask.

Quickstart
----------

First, install Flask-SimpleLDAP:
    
    $ pip install flask-simpleldap
    
Flask-SimpleLDAP depends, and will install for you, recent versions of Flask
(0.9 or later) and python-ldap. Flask-SimpleLDAP is compatible
with and tested on Python 2.6 and 2.7.

Next, add a ``LDAP`` instance to your code and at least the three
required configuration options:

```python
from flask import Flask
from flask.ext.simpleldap import LDAP

app = Flask(__name__)
ldap = LDAP(app)

app.config['LDAP_BASE_DN'] = 'OU=users,dc=example,dc=org'
app.config['LDAP_USERNAME'] = 'CN=user,OU=Users,DC=example,DC=org'
app.config['LDAP_PASSWORD'] = 'password'

@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'
```

You can take a look at [examples/groups](examples/groups) for a more complete 
example using LDAP groups.

You can also take a look at [examples/blueprints](examples/blueprints) for an 
example using Flask's 
[application factories](http://flask.pocoo.org/docs/patterns/appfactories/) 
and [blueprints](http://flask.pocoo.org/docs/blueprints/).


OpenLDAP
----------

Add the ``LDAP`` instance to your code and depending on your OpenLDAP
configuration, add the following at least LDAP_USER_OBJECT_FILTER and 
LDAP_USER_OBJECT_FILTER.

```python
from flask import Flask
from flask.ext.simpleldap import LDAP

app = Flask(__name__)
ldap = LDAP(app)

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
app.config['LDAP_GROUP_OBJECT_FILTER'] = "(&(objectclass=groupOfUniqueNames)(uniquemember=%s))"
app.config['LDAP_GROUP_MEMBER_FILTER'] = "(&(cn=*)(objectclass=groupOfUniqueNames)(uniquemember=%s))"
app.config['LDAP_GROUP_MEMBER_FILTER_FIELD'] = "cn"

@app.route('/ldap')
@ldap.login_required
def ldap_protected():
    return 'Success!'
```


Resources
---------

- [Documentation](http://flask-simpleldap.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SimpleLDAP)
