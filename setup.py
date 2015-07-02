#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-view-timer',
    version='0.1.4',
    description='Django View Timer',
    long_description=open('README.rst').read(),
    author='Alessio Di Stasio',
    author_email='aledista@gmail.com',
    url='https://github.com/aledista/django-view-timer',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'wrapt>=1.10',
        'termcolor==1.1.0',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    test_suite='runtests.runtests',
    extras_require={
        'tests': [
            'Django>=1.6',
            'flake8',
            'mock',
            'pytest',
        ],
    },
)
