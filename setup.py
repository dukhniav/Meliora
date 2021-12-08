#!/usr/bin/env python

from setuptools import setup, find_packages


long_description = open('README.md').read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.0.1'

setup(
    name='meliora',
    version=version,
    description='crypto portfolio tracker/balancer/analyzer',
    author='Duke Nasty',
    author_email='dukhnitskiy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    url='https://github.com/dukhniav/meliora',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
