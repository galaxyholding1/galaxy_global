from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="galaxy_global",
    version="0.0.1",
    author="Galaxy DevOps Team",
    author_email="devops@galaxynp.holdings",
    description="Galaxy Global Group - Corporate ERP Layer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GalaxyNP/galaxy-global-erpnext",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        "frappe",
    ],
    include_package_data=True,
    zip_safe=False,
)
