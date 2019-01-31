#!/usr/bin/env python
# Authors:
# - davidtavarez
# - D4Vinci
import requests
import argparse

session = requests.session()
session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
url = "http://pwndb2am4tzkvold.onion/"

G, B, R, W, M, C, end = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m'
info = end + W + "[+]" + W
good = end + G + "[+]" + C
bad = end + R + "[" + W + "!" + R + "]"


def main(args):
    if args.list:
        try:
            emails = open(args.list).readlines()
            print(info + " Connecting to pwndb service on tor network...")
            for email in emails:
                find(email.strip())
        except:
            print("[!] Can't read file " + str(args.list))
            exit(0)
    elif args.email:
        print(info + " Connecting to pwndb service on tor network...")
        find(args.email)
    else:
        print(bad + " You need to provide a target first!" + end)


def find(email):
    username = email
    domain = "%"
    if "@" in email and "." in email:
        username = email.split("@")[0]
        domain = email.split("@")[1]
    request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}
    try:
        r = session.post(url, data=request_data)
        results = parse(r.text)
        if not results:
            print(bad + " No leaks found for " + end + M + email)
            exit(0)
        for result in results:
            username = result.get('username', '')
            domain = result.get('domain', '')
            password = result.get('password', '')
            where = result.get('where', ' ')
            print(good + " Found " + username + "@" + domain + ":" + password + " " + where)
    except:
        print(bad + " Can't connect to service! restart tor service and try again")
        exit(0)


def parse(text):
    if "Array" not in text:
        return None

    leaks = text.split("Array")[1:]
    emails = []
    locations = {}
    for leak in leaks:
        leaked_email = leak.split("[luser] =>")[1].split("[")[0].strip()
        domain = leak.split("[domain] =>")[1].split("[")[0].strip()
        password = leak.split("[password] =>")[1].split(")")[0].strip()

        email = "{}@{}".format(leaked_email, domain)
        where = locations.get(email, None)
        if not where:
            where = "({})".format(verify_on_leakz(email))
            locations[email] = where

        emails.append({'username': leaked_email, 'domain': domain, 'password': password, 'where': where})
    return emails


def verify_on_leakz(email):
    try:
        url_api = "https://lea.kz/api/mail/{}".format(str(email))
        return session.get(url_api).json().get('leaked', '-')
    except:
        pass
    return ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pwndb.py')
    parser.add_argument("--email", help="Target email to search for leaks.")
    parser.add_argument("--list", help="A list of emails in a file to search for leaks.")
    args = parser.parse_args()

    main(args)
