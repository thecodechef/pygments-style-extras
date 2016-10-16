from setuptools import setup, find_packages

def read(fname):
  import os
  return open(os.path.join(os.path.dirname(__file__),fname)).read()


setup (
  name='pygments-style-extras',
  version='0.0.3',
  description='A Collection of Custom Pygments Styles',
  long_description=read('README.rst'),
  license='MIT',
  keywords='pygments style extras',

  author='Jeremy Bolding',
  author_email='cyberchefjay@gmail.com',

  url='https://github.com/thecodechef/pygments-style-extras',
  download_url='https://github.com/thecodechef/pygments-style-extras/tarball/0.0.3',


  packages=find_packages(),
  install_requires=['pygments >= 1.5'],
  
  entry_points =read('.pygments'),

  classifiers=[
    'Development Status :: 1 - Planning',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)