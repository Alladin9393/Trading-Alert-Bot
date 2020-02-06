"""
Setup the package.
"""
from setuptools import find_packages, setup

with open('README.md', 'r') as read_me:
    long_description = read_me.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    version='0.1.1',
    name='alertbot',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Alladin9393/alertbot',
    license='MIT',
    author='Alladin9393',
    author_email='ember.toon@protonmail.com',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'alertbot = alertbot.main:main',
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
