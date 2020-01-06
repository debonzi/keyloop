from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

requires = [
    "pyramid==1.10.4",
    "gunicorn==20.0.4",
    "marshmallow==3.3.0",
    "pymodm==0.4.2",
    "cryptacular==1.5.5",
    "cornice==4.0.1",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "WebTest==2.0.33",
]
ci_requires = [
    "python-coveralls",
]
dev_requires = ["black", "pre-commit"] + test_requires

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
    entry_points={
        "paste.app_factory": ["main = keyloop:main",],
        "console_scripts": ["kloop = keyloop.command.main:main"],
    },
)
