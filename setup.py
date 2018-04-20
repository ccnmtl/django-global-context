from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='django-global-context',
      version='0.1.1',
      description='Global context injector for Django',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Nik Nyby',
      author_email='nnyby@columbia.edu',
      url='https://github.com/ccnmtl/django-global-context',
      install_requires=['Django'],
      packages=['globalcontext'],
)
