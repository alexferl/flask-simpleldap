from flask import Blueprint
from ..extensions import ldap

foo = Blueprint("foo", __name__, url_prefix="/foo")


@foo.route("/group")
@ldap.group_required(groups=["Web Developers", "QA"])
def group():
    return "Group restricted page in foo module"
