import os
from subprocess import Popen, PIPE

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


def get_git_version(default="v1.0.0"):
    try:
        p = Popen(['git', 'describe', '--tags'], stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        line = line.strip()
        return line.decode()
    except:
        return default

with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(
    name='affil_schema',
    version=get_git_version(default="v1.0.0"),
    url='http://github.com/adsabs/augment_affil_data_model/',
    license="AGPL-3.0",
    author="Matthew Templeton",
    description='JSON Schema for SciX Honeycomb augmented affiliations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={'affil_schema': ['*.json']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9+',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
