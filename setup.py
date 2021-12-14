from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1.21", "Pillow>=8.4", "setuptools>=57", "scikit-image>=0.19","patchify>=0.2.3"]

setup(
    name="derm_ita",
    version="0.0.7",
    author="Adam Corbin",
    author_email="acorbin3@gmail.com",
    description="A package with different strategies to compute individual typology angle",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/acorbin3/derm_ita",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)