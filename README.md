# pwndb.py
pwndb.py is a Python command-line for searching leaked credentials using the Onion service with the same name.

## Usage

```
usage: pwndb.py [-h] [--target TARGET] [--list LIST]

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET  Target email/domain to search for leaks.
  --list LIST      A list of emails in a file to search for leaks.
```

> Note: tor service must be up and running to connect to it on port 9050

## Installation

Just create a virtualenv, install the requirements and make sure Tor is running.

```
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

usage: pwndb.py [-h] [--target TARGET] [--list LIST]

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET  Target email/domain to search for leaks.
  --list LIST      A list of emails in a file to search for leaks.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
