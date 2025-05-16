from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="python_kotprog",
    version="0.1.0",
    author="Petrányi Dominik (HHU7FQ)",
    author_email="petranyidominik0@gmail.com",
    description="A poker game developed for university python course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dominikcos7/python-kotprog",
    packages=find_packages(),
    py_modules=["main"],  # Include main.py in the project root
    include_package_data=True,
    package_data={
        'src': ['img/*.png', 'img/*.jpg', 'img/players/*.png', 'sound/*.mp3'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pygame",
        "treys",
    ],
    entry_points={
        'console_scripts': [
            'python_kotprog=main:main',
        ],
    },
)
