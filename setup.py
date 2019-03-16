
from setuptools import setup, find_packages

setup(name='aem',
      version='0.1',
      description='The funniest joke in the world',
      long_description='Really, the funniest around.',
      url='https://github.com/hejmsdz/aem',
      author='Mikołaj Rozwadowski',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
      ],
      include_package_data=True,
      zip_safe=False)
