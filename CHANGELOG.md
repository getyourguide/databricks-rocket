# Changelog db-rocket

## Version 3.0.0
- Add `use_volumes` and `dst_path` arguments to support uploading to Unity Catalog Volumes.

## Version 2.1.0
- New paramter for ``rocket launch --glob_path=<...>``, which allows to specify a list of globs for files to deploy during launch. 

## Version 2.0.4
- Update version number.

## Version 2.0.3
- Add instruction to restart Python with dbutils (needed for newer Databricks runtimes)

## Version 2.0.2
- fix wheel uploading to root dbfs path

## Version 2.0.1
- fix function not found error

## Version 2.0.0
- Simplify code structure
- Make sync of project more smooth by using a mix of `-e` & installation of `requirements.txt`

## Version 1.3.6

- Fix bug of updates not getting detected
- Put files into a project folder

## Version 1.3.5

- Replace self-calling CLI with while loop

## Version 1.3.4

- Simplify setup by using `pip install -e`

## Version 1.3.3

- Fix watch stopping due to maximum recursion

## Version 1.3.2

- Refine prints to be more clear

## Version 1.3.1

- Adding Markdown documentation to package description

## Version 1.3.0

- Remove `rocket trigger` CLI
- Add synchronization of project files to databricks file system
- Replace `print` statements with `logger.info`
- Replace running watch in shell with python code

## Version 1.2.0

- Fix security issue with command injection, changes the behaviour of the watch command.

## Version 1.1.5

- Adding extra index urls to install command

## Version 1.1.4

- Fix error in rocket trigger cmd

## Version 1.1.3

- Typo

## Version 1.1.2

- Pin watchdog dependency with minimum requirement
- dbrocket launch rather then trigger

## Version 1.1.1

- Error with token missing only on trigger command not on __init__ anymore.

## Version 1.1.0

- Create new binary dbrocket
- Create dbrocket setup to initalize a setup.py
- Use defualt values for trigger binary
- Improve docs

## Version 1.0.4

- Upgrade dependencies
- Add github actions ci.

## Version 1.0.3

- Remove message about spark 6 support.
- Add instruction about upgrading pip.
- Remove local cli.
- Add better error message when fails to copy to databricks

## Version 1.0.2

feature: Add support for poetry projects test: Add test for dbrocket build process
