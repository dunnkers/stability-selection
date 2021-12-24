#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='stability-selection',
      version='0.1.0',
      description='A scikit-learn compatible implementation of stability selection for feature selection',
      author='Thomas Huijskens',
      packages=find_packages(),
      install_requires=[
            "numpy>=1.19",
            "scikit-learn>=0.24",
      ],
      author_email='thomas_huijskens@hotmail.com',
      )
