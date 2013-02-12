# -*- coding: utf-8 *-*
try:
    from setuptools import setup
except ImportError:
    from distutils import setup


setup(
    name='ModuleName',
    version='0.1',
    description='Description',
    long_description='Long description',
    author='Me',
    author_email='me@domain.tld',
    packages=['module_name', 'test'],
    install_requires=['pymongo'],
    classifiers=["Intended Audience :: Developers"],
    setup_requires=['pymongo'],
    test_suite='unittest.main'
)
