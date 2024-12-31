from setuptools import setup, find_packages
# Read the contents of the README file for long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

from setuptools import setup, find_packages

# Read the contents of the README file for long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gtus",  
    version="0.1.0",  
    author="Levent Bulut",  
    author_email="levent.bulut@unt.edu",  
    description="A Python package for collecting Google Trends data across US states",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Markdown for PyPI
    url='https://github.com/leventbulut/gtus',
    keywords=['google trends', 'trends data', 'us states', 'regional data', 'search interest', 'data collection'],  
    packages=find_packages(),  # Automatically find package directories
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: MIT License',  
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Internet :: WWW/HTTP :: Browsers',
    'Topic :: Scientific :: Engineering :: Information Analysis',
    'Operating System :: OS Independent',
    ],
    python_requires=">=3.6",  # Specify minimum Python version
    install_requires=[
        "pandas>=1.0.0",
        "pytrends",
        "aiohttp>=3.7.0",
        "openpyxl",
        "xlsxwriter",
        "click",
        "PyGithub",
    ],  # List your dependencies
    extras_require={
        "dev": ["pytest", "flake8"],  # Add development dependencies
    },
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    entry_points={
        "console_scripts": [
            "gtus=gtus.core:main",  # Example entry point for CLI usage
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/gtus/issues",
        "Documentation": "https://github.com/yourusername/gtus/wiki",
        "Source Code": "https://github.com/yourusername/gtus",
    },
)
