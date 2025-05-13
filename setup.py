from setuptools import setup, find_packages

setup(
    name='dllib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tensorflow',
        'scikit-learn'
    ],
    author='sahith',
    description='A deep learning library with 10 educational programs',
)