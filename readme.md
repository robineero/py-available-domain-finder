### Available domain finder ###

**Does not work with .ee domains anymore due to the change of python whois library**

Simple scanner for available domain names written in Python.
Results are written into `domains-available.txt` file.

Does not work with .eu domains (which needs 1 sec sleep time between every request to avoid running into limit and gives false-positive results). Tested with .ee domains.
