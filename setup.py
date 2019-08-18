from setuptools import setup, find_packages

setup(
    name="tablero",
    version="0.1.0",
    packages=find_packages(),
    install_requires = [
        "flask",
        "numpy",
        "pandas",
    ]
)
