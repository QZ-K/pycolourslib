from setuptools import setup, find_packages

setup(
    name='colours_lib',
    version='0.1',
    packages=find_packages(),
    description='a python module with variabled colours for more simplicity and less time-wasting in your projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='KZed-K',
    author_email='kuzeykural040510@gmail.com',
    url='https://github.com/KZed-K/colours_lib', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
