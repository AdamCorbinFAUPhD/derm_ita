from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1.21", "Pillow>=8.4", "setuptools>=57", "scikit-image>=0.19","patchify>=0.2.3"]

extra_test = [
    'pytest>=4',
    'pytest-cov>=2',
]

extra_dev = [
    *extra_test,
]

setup(
    name="derm_ita",
    version="0.0.8",
    author="Adam Corbin",
    author_email="acorbin3@gmail.com",
    description="A package with different strategies to compute individual typology angle",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/acorbin3/derm_ita",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={

            'test': extra_test,
            'dev': extra_dev,
        },

    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)