from setuptools import setup, find_packages

setup(
    name='ca-api-wrapper',
    version='1.0.0',
    author='Vick Mu',
    author_email='arbi3400@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    description='A NON-OFFICIAL Python package for accessing the ChannelAdvisor RESTful API',
    long_description=open('README.md').read(),
    install_requires=[
        # Your package dependencies
    ],
)

from setuptools import setup, find_packages

setup(
    name='channeladvisor',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'pandas>=1.3.4',
        'numpy>=1.21.5',
    ],
    long_description=open('README.md').read(),
    url='https://github.com/yourgithubrepo/channeladvisor',  # Optional project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
)
