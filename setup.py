#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="ansible-runner-mqtt",
    version="1.0",
    author="Tyler Cross",
    url="https://github.com/wtcross/ansible-runner-mqtt",
    license='MIT',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['paho-mqtt'],
    entry_points={'ansible_runner.plugins': 'mqtt = ansible_runner_mqtt'},
    zip_safe=False,
)
