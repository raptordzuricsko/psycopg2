import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="psycopg2",
    version="1.2.1",
    author='Automation Team',
    author_email='automation@successacademies.org',
    url='http://automation.successacademies.org',
    description="A aws psycopg2 package from psycopg2.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
