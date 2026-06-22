from setuptools import setup, find_packages

setup(
    name="gitty-cache",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "redis",
    ],
)
