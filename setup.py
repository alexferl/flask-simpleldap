"""
Flask-SimpleLDAP
----------------

LDAP authentication extension for Flask
"""
from setuptools import setup


setup(
    name='Flask-SimpleLDAP',
    version='1.1.1',
    url='https://github.com/admiralobvious/flask-simpleldap',
    license='MIT',
    author='Alexandre Ferland',
    author_email='aferlandqc@gmail.com',
    description='LDAP authentication extension for Flask',
    long_description=__doc__,
    packages=['flask_simpleldap'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10.1',
        'pyldap'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
