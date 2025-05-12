from setuptools import setup, find_packages

setup(
    name="filder-info",
    version="0.1.0",
    author="Henoc N'GASAMA",
    author_email="ngasamah@gmail.com",
    description="A CLI tool to analyze files and folders with metadata, structure, and statistics.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/henocn/filder-info",
    project_urls={
        "Documentation": "https://github.com/henocn/filder-info",
        "Bug Tracker": "https://github.com/henocn/filder-info/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0"
    ],
    entry_points={
        "console_scripts": [
            "filder-info=filder_info.cli:main",
        ],
    },
    include_package_data=True,
)
