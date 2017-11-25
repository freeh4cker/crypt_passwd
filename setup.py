from setuptools import setup
# -*- coding: utf-8 -*-

##########################################################################
# Copyright (c) 2017 Bertrand Néron. All rights reserved.                #
# Use of this source code is governed by a BSD-style license that can be #
# found in the LICENSE file.                                             #
##########################################################################

setup(
    name='crypt_passwd',
    version='1.0',
    description='simple wrapper around passlib. Prompt for a password and encrypt it.',
    long_description=open('README.md').read(),
    author='freeh4cker',
    author_email='freeh4cker@gmail.com',
    license="GPLv3",
    keywords="password encryption",
    python_requires=">=3.3",
    install_requires=open("requirements.txt").read().split(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Topic :: Security :: Cryptography',
        ],
    platforms=['Unix', 'Linux', 'MacOsX'],
    scripts=['crypt_passwd'],
)


