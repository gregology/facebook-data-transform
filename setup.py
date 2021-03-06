from setuptools import setup, find_packages

setup(
  name='fbetl',
  version='0.1.2',
  description='',
  long_description=open('README.rst').read(),
  url='https://github.com/gregology/fbetl',
  author='Greg Clarke',
  author_email='greg@gho.st',
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
  ],
  keywords='facebook, data',
  packages=find_packages(),
  package_data={
    'fbetl': []
  }
)
