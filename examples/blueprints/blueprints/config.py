import ldap


class BaseConfig(object):
    PROJECT = "foo"
    SECRET_KEY = "dev key"
    DEBUG = True

    # LDAP
    # LDAP_HOST = "ldap.example.org"  # defaults to localhost
    LDAP_BASE_DN = "dc=example,dc=org"
    LDAP_USERNAME = "cn=admin,dc=example,dc=org"
    LDAP_PASSWORD = "admin"
    LDAP_LOGIN_VIEW = "core.login"
    LDAP_CUSTOM_OPTIONS = {ldap.OPT_REFERRALS: 0}
