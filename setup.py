import os

from setuptools import find_packages, setup

setup(name='vectorize',
      version='0.2.0',
      description="Vectorize functions.",
      #long_description=open('README.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      keywords='',
      author='Stijn Debrouwere',
      author_email='stijn@debrouwere.org',
      download_url='http://www.github.com/debrouwere/python-vectorize/tarball/master',
      license='ISC',
      #test_suite='vectorize.tests',
      packages=find_packages(),
      )
