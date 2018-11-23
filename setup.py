import os

from setuptools import setup, find_packages

__author__ = 'leifj'

here = os.path.abspath(os.path.dirname(__file__))
README_fn = os.path.join(here, 'README.rst')
README = 'smscom.se client'
if os.path.exists(README_fn):
    README = open(README_fn).read()

version = '0.6'

install_requires = [
    'six==1.11.0',
    'httplib2'
]

testing_extras = [
    'nose==1.3.7',
    'nosexcover==1.0.11',
    'coverage==4.5.1',
    'mock==2.0.0',
]

setup(
    name='pysmscom',
    version=version,
    description="python client for smscom.se (ip1.se) SMS gateway",
    long_description=README,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='SMS',
    author='Leif Johansson',
    author_email='leifj@sunet.se',
    url='http://github.com/SUNET/pysmscom',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    }
)
