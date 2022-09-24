import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greek-to-greeklish",
    version="0.0.4",
    author="Timotheos Savva",
    author_email="",
    description="Greek Letter Transliteration based on ELOT 743 standard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timossavva/greek-to-greeklish",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
