from setuptools import setup
from setuptools import find_packages

setup(
    name='print_color',
    version='0.1.0',
    packages=find_packages(include=['app', 'app.*']),
    description='A package to print colored messages in Python with ANSI codes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jean Olmedillo',
    author_email='info@jeanolmedillo.com',
    url='https://github.com/Jmofuture/printer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    test_suite='tests',
)
