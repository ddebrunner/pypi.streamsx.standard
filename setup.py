from setuptools import setup
setup(
  name = 'streamsx.standard',
  packages = ['streamsx.standard'],
  include_package_data=True,
  version = '0.1.1',
  description = 'IBM Streams Standard toolkit',
  long_description = open('DESC.txt').read(),
  author = 'IBM Streams @ github.com',
  author_email = 'debrunne@us.ibm.com',
  license='Apache License - Version 2.0',
  url = 'https://github.com/ddebrunner/pypi.streamsx.standard',
  keywords = ['streams', 'ibmstreams', 'streaming', 'analytics', 'streaming-analytics'],
  classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
  ],
  install_requires=['streamsx'],
  
  test_suite='nose.collector',
  tests_require=['nose']
)
