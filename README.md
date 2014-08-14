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

Check the [examples](examples/) folder for a more complex example using LDAP groups.


Resources
---------

- [Documentation](http://flask-simpleldap.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SimpleLDAP)
