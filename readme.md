### Available domain finder ###

Simple scanner for available domain names written in Python using [python-whois package](https://pypi.org/project/python-whois/) (0.7.3). Tested with .ee domains.
Results are written into `domains-available.txt` file.

Code does not work with .eu domains (which need 1 sec sleep time between every request to avoid running into limit and gives false-positive results).
