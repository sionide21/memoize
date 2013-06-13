#!/usr/bin/env python
from setuptools import setup


setup(
    name='memoize',
    version='1.0.0',
    author='Ben Olive',
    author_email='sionide21@gmail.com',
    description='Create properties that are only computed the first time they are called.',
    url='https://github.com/sionide21/memoize',

    py_modules=['memoize'],
    platforms='all',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
