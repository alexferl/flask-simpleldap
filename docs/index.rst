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

      pip install flask-simpleldap

Flask-SimpleLDAP depends, and will install for you, recent versions of Flask
(0.12.4 or later) and pyldap. Flask-SimpleLDAP is compatible
with and tested on Python 3.7+.

Next, add a :class:`~flask_simpleldap.LDAP` to your code and at least the three
required configuration options:

    .. code-block:: python

      from flask import Flask
      from flask_simpleldap import LDAP

      app = Flask(__name__)
      # app.config["LDAP_HOST"] = "ldap.example.org"  # defaults to localhost
      app.config["LDAP_BASE_DN"] = "OU=users,dc=example,dc=org"
      app.config["LDAP_USERNAME"] = "CN=user,OU=Users,DC=example,DC=org"
      app.config["LDAP_PASSWORD"] = "password"

      ldap = LDAP(app)

      @app.route("/ldap")
      @ldap.login_required
      def ldap_protected():
          return "Success!"


      if __name__ == "__main__":
          app.run()


Configuration
-------------

:class:`~flask_simpleldap.LDAP` understands the following configuration
directives:

================================== ================================================================
``LDAP_HOST``                      The host name or IP address of your LDAP server.
                                   Default: 'localhost'.
``LDAP_PORT``                      The port number of your LDAP server. Default: 389.
``LDAP_SCHEMA``                    The LDAP schema to use between 'ldap' and 'ldaps'.
                                   Default: 'ldap'.
``LDAP_USERNAME``                  **Required**: The user name used to bind.
``LDAP_PASSWORD``                  **Required**: The password used to bind.
``LDAP_TIMEOUT``                   How long (seconds) a connection can take to be opened
                                   before timing out. Default: 10.
``LDAP_USE_SSL``                   Set to ``True`` if your server uses SSL.
                                   Default: ``False``.
``LDAP_USE_TLS``                   Set to ``True`` if your server uses TLS.
                                   Default: ``False``.
``LDAP_REQUIRE_CERT``              Set to ``True`` if your server requires a certificate.
                                   Default: ``False``.
``LDAP_CERT_PATH``                 Path to the certificate if ``LDAP_REQUIRE_CERT`` is
                                   ``True``.
``LDAP_BASE_DN``                   **Required**: The distinguished name to use as the search base.
``LDAP_OBJECTS_DN``                The field to use as the objects' distinguished name.
                                   Default: 'distinguishedName'.
``LDAP_USER_FIELDS``               ``list`` of fields to return when searching for a user's
                                   object details. Default: ``list`` (all).
``LDAP_USER_OBJECT_FILTER``        The filter to use when searching for a user object.
                                   Default: '(&(objectclass=Person)(userPrincipalName=%s))'
``LDAP_USER_GROUPS_FIELD``         The field to return when searching for a user's
                                   groups. Default: 'memberOf'.
``LDAP_GROUPS_OBJECT_FILTER``      The filter to use when searching for groups objects.
                                   Default: 'objectclass=Group'
``LDAP_GROUP_FIELDS``              ``list`` of fields to return when searching for a group's
                                   object details. Default: ``list`` (all).
``LDAP_GROUP_OBJECT_FILTER``       The filter to use when searching for a group object.
                                   Default: '(&(objectclass=Group)(userPrincipalName=%s))'
``LDAP_GROUP_MEMBERS_FIELD``       The field to return when searching for a group's members.
                                   Default: 'member'
``LDAP_LOGIN_VIEW``                Views decorated with :meth:`.login_required()` or
                                   :meth:`.group_required()` will redirect
                                   unauthenticated requests to this view. Default:
                                   'login'.
``LDAP_REALM_NAME``                Views decorated with
                                   :meth:`.basic_auth_required()` will use this as
                                   the "realm" part of HTTP Basic Authentication when
                                   responding to unauthenticated requests.
``LDAP_OPENLDAP``                  Set to ``True`` if your server is running OpenLDAP.
                                   Default: ``False``
``LDAP_GROUP_MEMBER_FILTER``       The group member filter to use when using OpenLDAP.
                                   Default: '*'
``LDAP_GROUP_MEMBER_FILTER_FIELD`` The group member filter field to use when using OpenLDAP.
                                   Default: '*'
``LDAP_CUSTOM_OPTIONS``            ``dict`` of ldap options you want to set in this format: {option: value}.
                                   Default: ``None``
================================== ================================================================


API
===

Classes
-------

.. autoclass:: flask_simpleldap.LDAP
   :members:


History
-------

Changes:

- 1.4.0 July 16, 2019

  - This release drops support for `Python 2.7 <https://pythonclock.org/>`_. If you're still on Python 2.7, you can use `v1.3.3 <https://github.com/alexferl/flask-simpleldap/releases/tag/v1.3.3>`_.

  - Fixes:

    - `#62 <https://github.com/admiralobvious/flask-simpleldap/issues/62>`_ get_object_details returning None

- 1.3.0 July 14, 2019

  - Thanks to the contributors, this release fixes issues related to bind_user and fixes some issues related to filtering.

    - `#51 <https://github.com/admiralobvious/flask-simpleldap/pull/51>`_ Referral chasing crash

    - `#54 <https://github.com/admiralobvious/flask-simpleldap/pull/54>`_ Fixes #44 - Error in bind_user method, also fixes #60 and #61

    - `#56 <https://github.com/admiralobvious/flask-simpleldap/pull/56>`_ OpenLDAP section has Incorrect LDAP_GROUP_OBJECT_FILTER

    - `#57 <https://github.com/admiralobvious/flask-simpleldap/pull/57>`_ next vaule: Priority use request.full_path

    - `#59 <https://github.com/admiralobvious/flask-simpleldap/pull/59>`_ get_object_details to take query_filter and fallback to LDAP_USER_OBJECT_FILTER or LDAP_GROUP_OBJECT_FILTER


- 1.2.0 September 26, 2017

  - Changed get_group_members() and get_user_groups() returning strings instead of bytes in PY3.

- 1.1.2 July 17, 2017

  - Merge GitHub PR `#30 <https://github.com/admiralobvious/flask-simpleldap/pull/30>`_,
    Fix for python3
  - Fix decoding bytes in PY3 for @ldap.group_required.

- 1.1.1 April 10, 2017

  - Merge GitHub pull `#26 <https://github.com/admiralobvious/flask-simpleldap/pull/26>`_,
    Fix set_option call to LDAP for SSL CERT

- 1.1.0 June 7, 2016

  - Add the ability the pass any valid pyldap config options via the LDAP_CUSTOM_OPTIONS configuration directive.

- 1.0.1 June 5, 2016

  - Fix ldap filter import.

- 1.0.0 June 4, 2016

  - Python 3.x support. Switched from python-ldap to pyldap which is a fork with Python 3.x support.

- 0.4.0: September 5, 2015

  - Added support for OpenLDAP directories. Thanks to `@jm66 <https://github.com/jm66>`_ on GitHub.

- 0.3.0: January 21, 2015

  - Fix Github issue `#10 <https://github.com/admiralobvious/flask-simpleldap/issues/10>`_,
    Redirect users back to the page they originally requested after authenticating

  - Fix GitHub issue `#12 <https://github.com/admiralobvious/flask-simpleldap/issues/12>`_,
    Only trust .bind_user() with a non-empty password

- 0.2.0: December 7, 2014

  - Added HTTP Basic Authentication. Thanks to `@OptiverTimAll <https://github.com/optivertimall>`_ on GitHub.
  - Fix GitHub issue `#4 <https://github.com/admiralobvious/flask-simpleldap/issues/4>`_,
    User or group queries are vulnerable to LDAP injection.
    Make sure you update your filters to use '%s' instead of the old '{}'!

- 0.1.1: September 6, 2014

  - Fix GitHub issue `#3 <https://github.com/admiralobvious/flask-simpleldap/issues/3>`_,
    Not compatible with uppercase distinguished names.

- 0.1: August 9, 2014

  - Initial Release
