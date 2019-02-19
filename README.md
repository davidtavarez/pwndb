# pwndb.py

pwndb.py is a python command-line tool for searching leaked credentials using the Onion service with the same name.

## Usage

```bash
usage: pwndb.py [-h] [--target TARGET] [--list LIST] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET  Target email/domain to search for leaks.
  --list LIST      A list of emails in a file to search for leaks.
  --output OUTPUT  Return results as json/txt
```

> Note: tor service must be up and running to be connected to port 9050

## Installation

Just create a virtualenv, install the requirements and make sure Tor is running.

```bash
$ git clone https://github.com/davidtavarez/pwndb
Cloning into 'pwndb'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 10 (delta 2), reused 4 (delta 0), pack-reused 0
Unpacking objects: 100% (10/10), done.

$ cd pwndb

$ virtualenv venv
New python executable in /Users/davidtavarez/pwndb/venv/bin/python
Installing setuptools, pip, wheel...done.

$ source venv/bin/activate

(venv) $ pip install -r requirements.txt
Collecting PySocks==1.6.8 (from -r requirements.txt (line 1))
...

(venv) $ python pwndb.py -h

usage: pwndb.py [-h] [--target TARGET] [--list LIST] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET  Target email/domain to search for leaks.
  --list LIST      A list of emails in a file to search for leaks.
  --output OUTPUT  Return results as json/txt
```

## Contributing

Pull Requests are welcomed. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Disclaimer

```
[!] Legal disclaimer: Usage of pwndb.py for attacking targets without
prior mutual consent is illegal. It is the end user's responsibility
to obey all applicable local, state and federal laws. Developers assume
no liability and are not responsible for any misuse or damage caused.
```
