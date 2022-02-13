from flask import Flask, g, request, session, redirect, url_for
from flask_simpleldap import LDAP

app = Flask(__name__)
app.secret_key = "dev key"
app.debug = True

app.config["LDAP_OPENLDAP"] = True
app.config["LDAP_OBJECTS_DN"] = "dn"
app.config["LDAP_REALM_NAME"] = "OpenLDAP Authentication"
app.config["LDAP_HOST"] = "openldap.example.org"
app.config["LDAP_BASE_DN"] = "dc=users,dc=openldap,dc=org"
app.config["LDAP_USERNAME"] = "cn=user,ou=servauth-users,dc=users,dc=openldap,dc=org"
app.config["LDAP_PASSWORD"] = "password"
app.config["LDAP_USER_OBJECT_FILTER"] = "(&(objectclass=inetOrgPerson)(uid=%s))"

# Group configuration
app.config["LDAP_GROUP_MEMBERS_FIELD"] = "uniquemember"
app.config["LDAP_GROUP_OBJECT_FILTER"] = "(&(objectclass=groupOfUniqueNames)(cn=%s))"
app.config["LDAP_GROUPS_OBJECT_FILTER"] = "objectclass=groupOfUniqueNames"
app.config["LDAP_GROUP_FIELDS"] = ["cn", "entryDN", "member", "description"]
app.config[
    "LDAP_GROUP_MEMBER_FILTER"
] = "(&(cn=*)(objectclass=groupOfUniqueNames)(member=%s))"
app.config["LDAP_GROUP_MEMBER_FILTER_FIELD"] = "cn"

ldap = LDAP(app)


@app.before_request
def before_request():
    g.user = None
    if "user_id" in session:
        # This is where you'd query your database to get the user info.
        g.user = {}
        # Create a global with the LDAP groups the user is a member of.
        g.ldap_groups = ldap.get_user_groups(user=session["user_id"])


@app.route("/")
@ldap.login_required
def index():
    return "Successfully logged in!"


@app.route("/login", methods=["GET", "POST"])
def login():
    if g.user:
        return redirect(url_for("index"))
    if request.method == "POST":
        user = request.form["user"]
        passwd = request.form["passwd"]
        test = ldap.bind_user(user, passwd)
        if test is None or passwd == "":
            return "Invalid credentials"
        else:
            session["user_id"] = request.form["user"]
            return redirect("/")
    return """<form action="" method="post">
                user: <input name="user"><br>
                password:<input type="password" name="passwd"><br>
                <input type="submit" value="Submit"></form>"""


@app.route("/group")
@ldap.group_required(groups=["web-developers"])
def group():
    return "Group restricted page"


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
