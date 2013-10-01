import os

from setuptools import setup, find_packages

__author__ = 'leifj'

here = os.path.abspath(os.path.dirname(__file__))
README_fn = os.path.join(here, 'README.rst')
README = 'smscom.se client'
if os.path.exists(README_fn):
    README = open(README_fn).read()

version = '0.1dev'

install_requires = [
    'httplib2'
]

testing_extras = [
    'nose==1.2.1',
    'nosexcover==1.0.8',
    'coverage==3.6',
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
    },
    test_suite='pysmscom',
)
