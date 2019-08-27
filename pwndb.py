#!/usr/bin/env python
# Authors:
# - davidtavarez
# - D4Vinci

import sys 

import requests
import argparse
from email.utils import getaddresses
import json

from requests import ConnectionError

if sys.version_info >= (3, 0):
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

G, B, R, W, M, C, end = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m'
info = end + W + "[-]" + W
good = end + G + "[+]" + C
bad = end + R + "[" + W + "!" + R + "]"


def main(emails, output=None):
    if not output:
        print(info + " Searching for leaks...")

    results = []

    for email in emails:
        leaks = find_leaks(email.strip())
        if leaks:
            for leak in leaks:
                results.append(leak)

    if not results:
        if not output:
            print(bad + " No leaks found." + end)

    if not output or output == 'txt':
        for result in results:
            username = result.get('username', '')
            domain = result.get('domain', '')
            password = result.get('password', '')

            if not output:
                print(good + "\t" + username + "@" + domain + ":" + password)
            if output == 'txt':
                print(username + "@" + domain + ":" + password)
    if output == 'json':
        print(json.dumps(results))

def find_leaks(email):
    url = "http://pwndb2am4tzkvold.onion/"
    username = email
    domain = "%"

    if "@" in email:
        username = email.split("@")[0]
        domain = email.split("@")[1]
        if not username:
            username = '%'

    request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}

    r = session.post(url, data=request_data)

    return parse_pwndb_response(r.text)


def parse_pwndb_response(text):
    if "Array" not in text:
        return None

    leaks = text.split("Array")[1:]
    emails = []

    for leak in leaks:
        leaked_email = ''
        domain = ''
        password = ''
        try :
            leaked_email = leak.split("[luser] =>")[1].split("[")[0].strip()
            domain = leak.split("[domain] =>")[1].split("[")[0].strip()
            password = leak.split("[password] =>")[1].split(")")[0].strip()
        except:
            pass
        if leaked_email:
            emails.append({'username': leaked_email, 'domain': domain, 'password': password})
    return emails


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pwndb.py')
    parser.add_argument("--target", help="Target email/domain to search for leaks.")
    parser.add_argument("--list", help="A list of emails in a file to search for leaks.")
    parser.add_argument("--output", help="Return results as json/txt")
    parser.add_argument("--proxy", default='127.0.0.1:9050', type=str, help="Set Tor proxy (default: 127.0.0.1:9050)")
    args = parser.parse_args()

    # Tor proxy
    proxy = args.proxy
    session = requests.session()
    session.proxies = {'http': 'socks5h://{}'.format(proxy), 'https': 'socks5h://{}'.format(proxy)}

    if not args.list and not args.target:
        print(bad + " Missing parameters!" + end)
        parser.print_help()
        exit(-1)

    emails = []

    output = None
    if args.output:
        if args.output not in ['json', 'txt']:
            print(bad + " Output should be json or txt" + end)
            exit(-1)
        output = args.output

    if args.target:
        emails.append(args.target)

    if args.list:
        try:
            lines = open(args.list).readlines()
            for line in lines:
                for input in line.split(','):
                    addresses = getaddresses([input])
                    for address in addresses:
                        emails.append(str(addresses[0][1]).strip())
        except Exception as e:
            print(bad + " Can't read the file: " + str(args.list))
            exit(-1)
    try:
        main(emails, output)
    except ConnectionError:
        print(bad + " Can't connect to service! restart tor service and try again.")
    except Exception as e:
        print(bad + " " + e)
