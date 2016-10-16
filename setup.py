from setuptools import setup, find_packages
 
setup (
  name='pygments-style-extras',
  version='0.0.2',
  description='A Collection of Custom Pygments Styles',
  long_description='A Collection of Custom Pygments Styles',
  license='MIT',
  keywords='pygments style extras',

  author='Jeremy Bolding',
  author_email='cyberchefjay@gmail.com',

  url='https://github.com/thecodechef/pygments-style-extras',
  download_url='https://github.com/thecodechef/pygments-style-extras/tarball/0.0.2',


  packages=find_packages(),
  install_requires=['pygments >= 1.5'],
  
  entry_points =open('.pygments').read(),

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