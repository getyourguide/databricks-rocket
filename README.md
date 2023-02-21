## DB-Rocket

<img src="https://user-images.githubusercontent.com/2252355/173396060-8ebb3a33-f389-421d-bea4-afc01a078307.svg" width="100" height="100">

[![PyPI version](https://badge.fury.io/py/databricks-rocket.svg)](https://badge.fury.io/py/databricks-rocket)
![PyPI downloads](https://img.shields.io/pypi/dm/databricks-rocket)

Keep your local python scripts installed and in sync with a databricks notebook.
Every change on your local machine is automatically applied to the notebook.
Shortens the feedback loop to develop git based projects.
Removes the need to setup a local development environment.

## Installation

```sh
pip3 install databricks-rocket
```

Please sure your python interpreter is 3.7 or higher.

## Setup

You will need to authenticate with databricks. Under the hood we use the databricks cli, for more information you can view how to authenticate the databricks cli [here](https://docs.databricks.com/dev-tools/cli/index.html#set-up-authentication). Make sure you have the following databricks tokens exported in your environment.

```sh
export DATABRICKS_TOKEN="mydatabrickstoken"
export DATABRICKS_HOST="URL_FOR_DATABRICKS"
```

If your project is not a pip package already you have to turn it into one. You can use dbrocket to do that.

```sh
dbrocket setup
```

Will create a setup.py for you.

## Using db-rocket

```sh
dbrocket launch
```

The command returns the exact command you have to perform in your notebook next.

Example:

```sh
We are now building your Python repo as a library...
Done! in your notebook install the library by running:

%pip install --upgrade pip
%pip install /dbfs/temp/username/databricks_rocket-1.1.3-py3-none-any.whl --force-reinstall
```

Create a cell in a notebook and paste the content (example below).

![img_1.png](img_1.png)

## Support

- Databricks: >=7
- Python: >=3.7
- Tested on Platform: Linux, MacOs. Windows will probably not work but contributions are welcomed!

## Acknowledgments

- Thanks Leon Poli for the Logo :)
- Thanks Stephane Leonard for source-code and documentation improvements :)
- Thanks Malachi Soord for the CICD setup and README improvements

Contributions are welcomed!

# Security

For security issues please contact [security@getyourguide.com](mailto:security@getyourguide.com).

# Legal

db-rocket is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE.txt) for the full text.
