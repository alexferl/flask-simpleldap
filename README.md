# Flask-SimpleLDAP
Flask-SimpleLDAP provides LDAP authentication for Flask and is compatible with and tested on Python 3.10+.

## Quickstart
First, install Flask-SimpleLDAP:

```shell
pip install flask-simpleldap
```

Flask-SimpleLDAP depends, and will install for you, a recent version of Flask
(2.2.5 or later) and [python-ldap](https://python-ldap.org/).
Please consult the [python-ldap installation instructions](https://www.python-ldap.org/en/latest/installing.html) if you get an error during installation.

Next, add an `LDAP` instance to your code and at least the three
required configuration options. The complete sample from
[examples/basic_auth/app.py](examples/basic_auth/app.py) looks like this:

```python
from flask import Flask, g
from flask_simpleldap import LDAP

app = Flask(__name__)
# app.config["LDAP_HOST"] = "ldap.example.org"  # defaults to localhost
app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
app.config["LDAP_PASSWORD"] = "password"

ldap = LDAP(app)

@app.route("/")
@ldap.basic_auth_required
def index():
    return f"Welcome, {g.ldap_username}!"

if __name__ == "__main__":
    app.run()
```

When the user visits the protected URL, the browser will prompt for the
login and password via the built-in HTTP authentication window. Note that
with the default value of `LDAP_USER_OBJECT_FILTER` the login is expected
to match the [`userPrincipalName` attribute](https://ldapwiki.com/wiki/Wiki.jsp?page=UserPrincipalName)
of the LDAP user, e.g. `me@mydomain.com`.

Once you get the basic example working, check out the more complex ones:

- [examples/groups](examples/groups) demonstrates using:
  - `@ldap.login_required` for form/cookie-based auth, instead of basic HTTP authentication.
  - `@ldap.group_required()` to restrict access to pages based on the user's LDAP groups.
- [examples/blueprints](examples/blueprints) implements the same functionality, but uses Flask's
[application factories](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/)
and [blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/).


## OpenLDAP
Add the `LDAP` instance to your code and depending on your OpenLDAP
configuration, add the following at least `LDAP_USER_OBJECT_FILTER` and
`LDAP_USER_OBJECT_FILTER`.

```python
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
app.config["LDAP_OBJECTS_DN"] = "dn"
app.config["LDAP_OPENLDAP"] = True
app.config["LDAP_USER_OBJECT_FILTER"] = "(&(objectclass=inetOrgPerson)(uid=%s))"

# Groups
app.config["LDAP_GROUP_MEMBERS_FIELD"] = "uniquemember"
app.config["LDAP_GROUP_OBJECT_FILTER"] = "(&(objectclass=groupOfUniqueNames)(cn=%s))"
app.config["LDAP_GROUP_MEMBER_FILTER"] = "(&(cn=*)(objectclass=groupOfUniqueNames)(uniquemember=%s))"
app.config["LDAP_GROUP_MEMBER_FILTER_FIELD"] = "cn"

ldap = LDAP(app)

@app.route("/")
@ldap.basic_auth_required
def index():
    return f"Welcome, {g.ldap_username}!"

if __name__ == "__main__":
    app.run()
```

## Configuration
| Setting                          | Description                                                                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `LDAP_HOST`                      | The host name or IP address of your LDAP server. Default: `"localhost"`.                                                                                  |
| `LDAP_PORT`                      | The port number of your LDAP server. Default: `389`.                                                                                                      |
| `LDAP_SCHEMA`                    | The LDAP schema to use between `"ldap"`, `"ldapi"` and `"ldaps"`. Default: `"ldap"`.                                                                      |
| `LDAP_SOCKET_PATH`               | If `LDAP_SCHEMA` is set to `"ldapi"`, the path to the Unix socket path. Default: `"/"`.                                                                   |
| `LDAP_USERNAME`                  | **Required**: The username used to bind.                                                                                                                  |
| `LDAP_PASSWORD`                  | **Required**: The password used to bind.                                                                                                                  |
| `LDAP_TIMEOUT`                   | How long (seconds) a connection can take to be opened before timing out. Default: `10`.                                                                   |
| `LDAP_LOGIN_VIEW`                | Views decorated with `.login_required()` or`.group_required()` will redirect unauthenticated requests to this view. Default: `"login"`.                   |
| `LDAP_REALM_NAME`                | Views decorated with `.basic_auth_required()` will use this as the "realm" part of HTTP Basic Authentication when responding to unauthenticated requests. |
| `LDAP_OPENLDAP`                  | Set to `True` if your server is running OpenLDAP. Default: `False`.                                                                                       |
| `LDAP_USE_SSL`                   | Set to `True` if your server uses SSL. Default: `False`.                                                                                                  |
| `LDAP_USE_TLS`                   | Set to `True` if your server uses TLS. Default: `False`.                                                                                                  |
| `LDAP_REQUIRE_CERT`              | Set to `True` if your server requires a certificate. Default: `False`.                                                                                    |
| `LDAP_CERT_PATH`                 | Path to the certificate if `LDAP_REQUIRE_CERT` is `True`.                                                                                                 |
| `LDAP_CUSTOM_OPTIONS`            | `dict` of ldap options you want to set in this format: `{option: value}`. Default: `None`.                                                                |
| `LDAP_BASE_DN`                   | **Required**: The distinguished name to use as the search base.                                                                                           |
| `LDAP_OBJECTS_DN`                | The field to use as the objects' distinguished name. Default: `"distinguishedName"`.                                                                      |
| `LDAP_USER_FIELDS`               | `list` of fields to return when searching for a user's object details. Default: `[]` (all).                                                               |
| `LDAP_USER_GROUPS_FIELD`         | The field to return when searching for a user's groups. Default: `"memberOf"`.                                                                            |
| `LDAP_USER_OBJECT_FILTER`        | The filter to use when searching for a user object. Default: `"(&(objectclass=Person)(userPrincipalName=%s))"`                                            |
| `LDAP_USERS_OBJECT_FILTER`       | The filter to use when searching for users objects. Default: `"objectclass=Person"`                                                                       |
| `LDAP_GROUP_FIELDS`              | `list` of fields to return when searching for a group's object details. Default: `[]` (all).                                                              |
| `LDAP_GROUP_MEMBER_FILTER`       | The group member filter to use when using OpenLDAP. Default: `"*"`.                                                                                       |
| `LDAP_GROUP_MEMBER_FILTER_FIELD` | The group member filter field to use when using OpenLDAP. Default: `"*"`.                                                                                 |
| `LDAP_GROUP_MEMBERS_FIELD`       | The field to return when searching for a group's members. Default: `"member"`.                                                                            |
| `LDAP_GROUP_OBJECT_FILTER`       | The filter to use when searching for a group object. Default: `"(&(objectclass=Group)(userPrincipalName=%s))"`.                                           |
| `LDAP_GROUPS_OBJECT_FILTER`      | The filter to use when searching for groups objects. Default: `"objectclass=Group"`.                                                                      |
