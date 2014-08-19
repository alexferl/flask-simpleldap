class BaseConfig(object):
    PROJECT = 'foo'
    SECRET_KEY = 'dev key'
    DEBUG = True

    # LDAP
    LDAP_HOST = 'ldap.example.org'
    LDAP_BASE_DN = 'OU=users,dc=example,dc=org'
    LDAP_USERNAME = 'CN=user,OU=Users,DC=example,DC=org'
    LDAP_PASSWORD = 'password'
    LDAP_LOGIN_VIEW = 'core.login'
