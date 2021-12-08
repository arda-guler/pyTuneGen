import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytunegen",
    version="1.1.1",
    author="arda-guler",
    author_email="ardaguler09@gmail.com",
    description="Generates randomized music tunes with Python, with MIDI export support.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arda-guler/pyTuneGen",
    project_urls={
        "Bug Tracker": "https://github.com/arda-guler/pyTuneGen/issues",
        "Documentation": "https://arda-guler.github.io/pytunegenDocs/index.html",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=["midiutil"],
    python_requires=">=3.6",
)
