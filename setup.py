from distutils.core import setup
from setuptools import find_packages


if __name__ == '__main__':
    setup(
        name='Logjam',
        version='0.1.0',
        packages=find_packages(),
        author='Kent Howard',
        #install_requires=requires,
        include_package_data=True
    )
