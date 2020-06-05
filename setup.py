# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='ansitoimg',
    version='2020',
    description='Convert an ansi string to an image. Great for adding terminal output into a readme.',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/AnsiToImg/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/AnsiToImg",
        "repository":
            "https://github.com/FHPythonUtils/AnsiToImg"
    },
    author='FredHappyface',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=['ansitoimg'],
    package_dir={"": "."},
    package_data={"ansitoimg": ["*.yml"]},
    install_requires=['pyyaml==5.*,>=5.3.1', 'svgwrite==1.*,>=1.4.0'],
)
