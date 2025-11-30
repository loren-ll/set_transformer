from setuptools import setup, find_packages

setup(
    name="set_transformer",
    version="0.1",
    packages=find_packages(include=["set_transformer", "set_transformer.*"]),
    install_requires=[
        "torch",
    ],
)

