from setuptools import setup, find_packages

setup(
    name='eth_address_generator',
    version='0.1.0',
    author='ClarenceDan',
    author_email='tangdan0854@gmail.com',
    packages=find_packages(),
    description='A simple package to generate Ethereum addresses',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/clarencedan/eth_address_generator',
    install_requires=[
        'eth-keys',
        'secrets',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
