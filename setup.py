import setuptools

# load the README file and use it as the long_description for PyPI
try:
    with open("README.md", encoding="utf8") as f:
        readme = f.read()
except Exception as e:
    readme = ""

setuptools.setup(
    name="databricks-rocket",
    version="3.0.2",
    author="GetYourGuide",
    author_email="engineering.data-products@getyourguide.com",
    description="Keep your local python scripts installed and in sync with a databricks notebook. Shortens the feedback loop to develop projects using a hybrid enviroment",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/getyourguide/db-rocket",
    packages=setuptools.find_packages(),
    install_requires=["fire", "watchdog~=2.1.9", "build", "databricks_cli", "databricks-sdk==0.36.0"],
    entry_points={
        "console_scripts": ["rocket=rocket.rocket:main", "dbrocket=rocket.rocket:main"]
    },
    license="Apache 2.0",
)
