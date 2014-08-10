.. Flask-SimpleLDAP documentation master file, created by
   sphinx-quickstart on Sat Aug  9 19:44:30 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-SimpleLDAP's documentation!
============================================

Flask-SimpleLDAP provides LDAP authentication for Flask.


Quickstart
----------

First, install Flask-SimpleLDAP:

.. code-block:: bash

    $ pip install flask-simpleldap

Flask-SimpleLDAP depends, and will install for you, recent versions of Flask
(0.9 or later) and python-ldap. Flask-SimpleLDAP is compatible
with and tested on Python 2.6 and 2.7.

Next, add a :class:`~flask_simpleldap.LDAP` to your code and at least the three
required configuration options:

.. code-block:: python

    from flask import Flask
    from flask.ext.simpleldap import LDAP

    app = Flask(__name__)
    ldap = LDAP(app)

    app.config['LDAP_BASE_DN'] = 'OU=users,dc=example,dc=org'
    app.config['LDAP_USERNAME'] = 'CN=user,OU=Users,DC=example,DC=org'
    app.config['LDAP_PASSWORD'] = 'password'


Configuration
-------------

:class:`~flask_simpleldap.LDAP` understands the following configuration
directives:

============================ ===================================================
``LDAP_HOST``                The host name or IP address of your LDAP server.
                             Default: 'localhost'.
``LDAP_PORT``                The port number of your LDAP server. Default: 389.
``LDAP_SCHEMA``              The LDAP schema to use between 'ldap' and 'ldaps'.
                             Default: 'ldap'.
``LDAP_USERNAME``            **Required**: The user name used to bind.
``LDAP_PASSWORD``            **Required**: The password used to bind.
``LDAP_TIMEOUT``             How long (seconds) a connection can take to be opened
                             before timing out. Default: 10.
``LDAP_USE_SSL``             Set to ``True`` if your server uses SSL.
                             Default: ``False``.
``LDAP_USE_TLS``             Set to ``True`` if your server uses TLS.
                             Default: ``False``.
``LDAP_REQUIRE_CERT``        Set to ``True`` if your server requires a certificate.
                             Default: ``False``.
``LDAP_CERT_PATH``           Path to the certificate if ``LDAP_REQUIRE_CERT`` is
                             ``True``.
``LDAP_BASE_DN``             **Required**: The distinguished name to use as the search base.
``LDAP_OBJECTS_DN``          The field to use as the objects' distinguished name.
                             Default: 'distinguishedName'.
``LDAP_USER_FIELDS``         ``list`` of fields to return when searching for a user's
                             object details. Default: ``list`` (all).
``LDAP_USER_OBJECT_FILTER``  The filter to use when searching for a user object.
                             Default: '(&(objectclass=Person)(userPrincipalName={}))'
``LDAP_USER_GROUPS_FIELD``   The field to return when searching for a user's
                             groups. Default: 'memberOf'.
``LDAP_GROUP_FIELDS``        ``list`` of fields to return when searching for a group's
                             object details. Default: ``list`` (all).
``LDAP_GROUP_OBJECT_FILTER`` The filter to use when searching for a group object.
                             Default: '(&(objectclass=Group)(userPrincipalName={}))'
``LDAP_GROUP_MEMBERS_FIELD`` The field to return when searching for a group's members.
                             Default: 'member'
``LDAP_LOGIN_VIEW``          The view to redirect to when a user needs to log-in.
                             Default: 'login'.
============================ ===================================================


API
===

Classes
-------

.. autoclass:: flask_simpleldap.LDAP
   :members:
