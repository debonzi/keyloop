#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

requires = [
    "pyramid==1.10.4",
    "gunicorn==20.0.4",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "tox",
]
ci_requires = [
    "python-coveralls",
]
dev_requires = test_requires + ["black", "pre-commit"]

extras_require = {
    "dev": dev_requires,
    "test": test_requires,
    "ci": ci_requires,
}

setup(
    name="keyloop",
    version="0.0.1",
    description="Key Loop - Authorization Server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Debonzi",
    author_email="debonzi@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=requires,
    extras_require=extras_require,
    url="https://github.com/debonzi/keyloop",
    packages=["keyloop",],
    entry_points={"paste.app_factory": ["main = keyloop:main",],},
)
