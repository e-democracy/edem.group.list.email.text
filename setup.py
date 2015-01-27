# -*- coding=utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(
    name='edem.group.list.email.text',
    version=version,
    description="E-Democracy customization of plain text messages in a "
                "group",
    long_description=open("README.txt").read() + "\n" +
    open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later "
        "(GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Bill Bushey',
    author_email='bill.bushey@e-democracy.org',
    url='https://github.com/e-democracy/edem.group.list.email.text',
    license='GPL 3',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edem', 'edem.group', 'edem.group.list',
                        'edem.group.list.email'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.tal',
        'zope.tales',
        'zope.viewlet',
        'edem.skin',
        'gs.group.list.email.text'
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
