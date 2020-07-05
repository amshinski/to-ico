import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="to-ico",
    version="1.1",
    author="amshinski",
    author_email="amshinski@gmail.com",
    description="A small png to ico convertor script.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amshinski/to-ico",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['to-ico=to_ico:main']
    },
)