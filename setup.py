import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-openid-client", # Replace with your own username
    version="0.1dev",
    author="Ben Collier",
    author_email="bencollier@fastmail.com",
    description="OIDC client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmcollier/python-openid-client",
    project_urls={
        "Bug Tracker": "https://github.com/bmcollier/python-openid-client",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)