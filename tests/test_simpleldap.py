import pytest
from flask import Flask
from flask_simpleldap import LDAP, LDAPException


def test_instantiate():
    app = Flask(__name__)
    app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
    app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
    app.config["LDAP_PASSWORD"] = "password"
    LDAP(app)


def test_instantiate_no_dn():
    app = Flask(__name__)
    with pytest.raises(LDAPException, match="LDAP_BASE_DN cannot be None!"):
        LDAP(app)


def test_instantiate_no_username():
    app = Flask(__name__)
    app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
    with pytest.raises(LDAPException, match="LDAP_USERNAME cannot be None!"):
        LDAP(app)


def test_instantiate_no_password():
    app = Flask(__name__)
    app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
    app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
    with pytest.raises(LDAPException, match="LDAP_PASSWORD cannot be None!"):
        LDAP(app)
