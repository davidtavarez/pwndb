# pwndb
Search for leaked creadentials on pwndb using the command line and tor.

## Usage:
```
usage: pwndb.py [-h] [--email EMAIL] [--list LIST]

optional arguments:
  -h, --help     show this help message and exit
  --email EMAIL  Target email to search for leaks.
  --list LIST    A list of emails in a file to search for leaks.
```

> Note: Of course,tor service must be up and running to connect to it on port 9050

## Using full email

```
(venv) > $ python pwndb.py --email info@fbi.gov
[+] Connecting to pwndb service on tor network...
[+] Found info@FBI.gov:fbi666
[+] Found info@fbi.gov:fbi666
````

## Using wildcard

```
(venv) > $ python pwndb.py --email therealdonald%
[+] Connecting to pwndb service on tor network...
[+] Found therealdonald99@gmail.com:bleed1
[+] Found THEREALDONALDTRUMP@HOTMAIL.COM:sergio22
````
## Using without domain

```
(venv) > $ python pwndb.py --email therealdonaldtrump
[+] Connecting to pwndb service on tor network...
[+] Found THEREALDONALDTRUMP@HOTMAIL.COM:sergio22
````