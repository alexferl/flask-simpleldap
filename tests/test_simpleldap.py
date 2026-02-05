import unittest

from flask import Flask

from flask_simpleldap import LDAP, LDAPException


class TestLDAP(unittest.TestCase):
    def test_instantiate(self):
        app = Flask(__name__)
        app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
        app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
        app.config["LDAP_PASSWORD"] = "password"
        LDAP(app)

    def test_instantiate_no_dn(self):
        app = Flask(__name__)
        with self.assertRaisesRegex(LDAPException, "LDAP_BASE_DN cannot be None!"):
            LDAP(app)

    def test_instantiate_no_username(self):
        app = Flask(__name__)
        app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
        with self.assertRaisesRegex(LDAPException, "LDAP_USERNAME cannot be None!"):
            LDAP(app)

    def test_instantiate_no_password(self):
        app = Flask(__name__)
        app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
        app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
        with self.assertRaisesRegex(LDAPException, "LDAP_PASSWORD cannot be None!"):
            LDAP(app)


if __name__ == "__main__":
    unittest.main()
