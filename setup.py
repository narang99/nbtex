from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nbtex",
    version="1.0.7",
    author="Hariom Narang",
    author_email="hariom2711@gmail.com",
    packages=find_packages(),
    url="https://github.com/narang99/nbtex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    description="A light-weight wrapper around LaTeX for mathematical symbols for Jupyter Notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
