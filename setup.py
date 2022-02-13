"""
Flask-SimpleLDAP
----------------

LDAP authentication extension for Flask
"""
from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="Flask-SimpleLDAP",
    version="1.4.0",
    url="https://github.com/alexferl/flask-simpleldap",
    license="MIT",
    author="Alexandre Ferland",
    author_email="me@alexferl.com",
    description="LDAP authentication extension for Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["flask_simpleldap"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask>=0.12.4", "python-ldap>=3.0.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
