from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ca_api_wrapper',
    version='1.0.0',
    author='Vick Mu',
    author_email='arbi3400@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    description='A NON-OFFICIAL Python package for accessing the ChannelAdvisor RESTful API',
    long_description=open('README.md').read(),
    long_description=long_description,
    long_description_content_type='text/markdown',
)

