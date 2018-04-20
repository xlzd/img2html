#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='img2html',
    version='0.0.7',
    author='xlzd',
    author_email='i@xlzd.me',
    description='Convert image to HTML',
    url='https://github.com/xlzd/img2html',
    license='WTFPL',
    packages=['img2html'],
    install_requires=[
        'jinja2',
        'pillow'
    ],
    entry_points={
        'console_scripts': [
            'img2html=img2html:main'
        ]
    }
)
