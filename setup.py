import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="greek-to-greeklish",
    version="0.0.8",
    author="Timotheos Savva",
    author_email="",
    description="Greek Letter Transliteration based on ELOT 743 standard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timossavva/greek-to-greeklish",
    packages=setuptools.find_packages(),
    install_requires=[
        'Js2Py==0.71'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
