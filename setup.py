from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'The Printer package provides a simple way to print messages with ANSI colors and styles in Python.'
PACKAGE_NAME= 'printstyler'
AUTHOR = 'Jean Olmedillo'
EMAIL= 'jeanolmedillo@outlook.com'
GITHUB_URL = 'https://github.com/Jmofuture/printer'

setup(
    name='printstyler',
<<<<<<< HEAD
    version='0.1.1',
=======
    version='0.1.0',
>>>>>>> 14c2b77bdc46ea88b78a6ac4c112910d3c6af035
    packages=[PACKAGE_NAME],
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=GITHUB_URL,
    keywords = [
        'print', 'printer', 'printstyler',
    ],
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
