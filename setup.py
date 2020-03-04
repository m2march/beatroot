#!/usr/bin/env python

import os
from subprocess import Popen

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        Popen(['make', '-C', 'beatroot'])
        install.do_egg_install(self)
        install.run(self)

class PostDevelopCommand(develop):
    def run(self):
        Popen(['make', '-C', 'beatroot'])
        develop.run(self)

setup(name='beatroot',
      version='0.1',
      description='API for beatroot for use from python',
      author='Martin "March" Miguel',
      author_email='m2.march@gmail.com',
      packages=['m2', 'm2.beatroot'],
      namespace_packages=['m2'],
      scripts=['scripts/beatroot'],
      package_data={
          'm2.beatroot': ['*.jar']
      },
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand
      },
      install_requires=[
          'numpy',
          'scipy'
      ]
)
