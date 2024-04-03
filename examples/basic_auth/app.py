from flask import Flask, g
from flask_simpleldap import LDAP

app = Flask(__name__)
#app.config["LDAP_HOST"] = "ldap.example.org"  # defaults to localhost
app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
app.config["LDAP_PASSWORD"] = "password"
app.config["LDAP_USER_OBJECT_FILTER"] = "(&(objectclass=inetOrgPerson)(uid=%s))"
app.config["LDAP_USERS_OBJECT_FILTER"] = "objectclass=inetOrgPerson"
app.config["LDAP_USER_FIELDS"] = ["cn", "uid"]

ldap = LDAP(app)


@app.route("/")
@ldap.basic_auth_required
def index():
    return "Welcome, {0}!".format(g.ldap_username)


if __name__ == "__main__":
    app.run()
