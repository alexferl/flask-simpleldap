from flask import Flask, g
from flask_simpleldap import LDAP

app = Flask(__name__)

# Base
app.config["LDAP_REALM_NAME"] = "OpenLDAP Authentication"
app.config["LDAP_HOST"] = "openldap.example.org"
app.config["LDAP_BASE_DN"] = "dc=users,dc=openldap,dc=org"
app.config["LDAP_USERNAME"] = "cn=user,ou=servauth-users,dc=users,dc=openldap,dc=org"
app.config["LDAP_PASSWORD"] = "password"

# OpenLDAP
app.config["LDAP_OPENLDAP"] = True
app.config["LDAP_OBJECTS_DN"] = "dn"
app.config["LDAP_USER_OBJECT_FILTER"] = "(&(objectclass=inetOrgPerson)(uid=%s))"
app.config["LDAP_USERS_OBJECT_FILTER"] = "objectclass=inetOrgPerson"

# Groups configuration
app.config["LDAP_GROUP_MEMBERS_FIELD"] = "uniquemember"
app.config["LDAP_GROUP_OBJECT_FILTER"] = "(&(objectclass=groupOfUniqueNames)(cn=%s))"
app.config["LDAP_GROUPS_OBJECT_FILTER"] = "objectclass=groupOfUniqueNames"
app.config["LDAP_GROUP_FIELDS"] = ["cn", "entryDN", "member", "description"]
app.config[
    "LDAP_GROUP_MEMBER_FILTER"
] = "(&(cn=*)(objectclass=groupOfUniqueNames)(member=%s))"
app.config["LDAP_GROUP_MEMBER_FILTER_FIELD"] = "cn"

ldap = LDAP(app)


@app.route("/")
@ldap.basic_auth_required
def index():
    return "Welcome, {0}!".format(g.ldap_username)


if __name__ == "__main__":
    app.run()
