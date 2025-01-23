from setuptools import setup, find_packages

setup(
    name="telegram", 
    version='1.0.0',
    author='Lucas Biason',
    packages=find_packages(),
    install_requires=[
        'telepot==12.7',
        'requests==2.23.0'
    ]
)