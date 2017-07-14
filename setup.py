# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    LDESC = open('README.md', 'r').read()
    LDESC = pypandoc.convert(LDESC, 'rst', format='md')
except (ImportError, IOError, RuntimeError) as e:
    print("Could not create long description:")
    print(str(e))
    LDESC = ''

setup(name='pt100',
      version = '0.1',
      description = 'Python package with different calculation algorithms for Pt100 temperature sensors',
      long_description = LDESC,
      author = 'Philipp Klaus',
      author_email = 'philipp.l.klaus@web.de',
      url = 'https://github.com/pklaus/python_pt100',
      license = 'GPL',
      packages = ['pt100',],
      #entry_points = {
      #    'console_scripts': [
      #        'pt100_conv = pt100.conv:main',
      #    ],
      #},
      zip_safe = True,
      platforms = 'any',
      install_requires = [
          #"numpy",
      ],
      extras_require = {
          'vectorized_calcs':  ["numpy",],
      },
      keywords = 'Pt100 temperature sensors',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Visualization',
      ]
)
