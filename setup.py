from setuptools import setup, find_packages

setup(
    name='kosapy',
    version='0.1',
    author='martinjr',
    description='KosAPI client lib for Python 3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests_cache'
    ],
)
