#!/usr/bin/env python

from subprocess import Popen

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

class PostInstallCommand(install):
    def run(self):
        Popen(['make', '-C', 'm2/beatroot'])
        install.run(self)

class PostDevelopCommand(develop):
    def run(self):
        Popen(['make', '-C', 'm2/beatroot'])
        develop.run(self)

setup(name='beatroot',
      version='0.1',
      description='API for beatroot for use from python',
      author='Martin "March" Miguel',
      author_email='m2.march@gmail.com',
      packages=['m2.beatroot'],
      namespace_packages=['m2'],
      scripts=['scripts/beatroot'],
      package_data={
          'm2.beatroot': ['m2/beatroot/BeatRoot.jar']
      },
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand
      }
)
