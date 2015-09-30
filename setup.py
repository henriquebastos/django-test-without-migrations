# coding: utf-8
from setuptools import setup
import os


setup(name='django-test-without-migrations',
      version='0.3',
      description='Disable migrations when running your Django tests.',
      long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      packages=[
          'test_without_migrations',
          'test_without_migrations.management',
          'test_without_migrations.management.commands',
          ],
      install_requires=[],
      zip_safe=True,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/henriquebastos/django-test-without-migrations/',
)
