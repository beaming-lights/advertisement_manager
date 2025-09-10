from setuptools import setup, find_packages

setup(
    name="advertisement_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'nicegui',
        'python-multipart',
        'python-magic',
    ],
    python_requires='>=3.7',
)
