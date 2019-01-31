#!/usr/bin/env python
# Authors:
# - davidtavarez
# - D4Vinci
import requests, argparse

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'
url = "http://pwndb2am4tzkvold.onion/"

G,B,R,W,M,C,end= '\033[92m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
info = end+W+"[+]"+W
bad  = end+R+"["+W+"!"+R+"]"
good = end+G+"[+]"+C
bad  = end+R+"["+W+"!"+R+"]"

def main(args):
    if args.list:
        try:
            emails = open(args.list).readlines()
        except:
            print("[!] Can't read file "+str(args.list))
            exit(0)
        print(info + " Connecting to pwndb service on tor network...")
        for email in emails:
            find(email.strip())
    elif args.email:
        print(info + " Connecting to pwndb service on tor network...")
        find(args.email)
    else:
        print(bad+" You need to provide a target first!"+end)

def find(email):
    username = email
    domain = "%"
    if "@" in email and "." in email:
        username = email.split("@")[0]
        domain = email.split("@")[1]
    request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}
    try:
        r = session.post(url,data=request_data)
        parse(r.text, email)
    except:
        print(bad+" Can't connect to service! restart tor service and try again")
        exit(0)
        
def parse(text,email):
    if "Array" not in text:
        print(bad+" No leaks found for "+end+M+email)
    else:
        leaks = text.split("Array")[1:]
        for leak in leaks:
            leak_mail = leak.split("[luser] =>")[1].split("[")[0].strip() + "@" + leak.split("[domain] =>")[1].split("[")[0].strip()
            print(good+" Found "+leak_mail+":"+leak.split("[password] =>")[1].split(")")[0].strip() )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pwndb.py')
    parser.add_argument("--email", help="Target email to search for leaks.")
    parser.add_argument("--list", help="A list of emails in a file to search for leaks.")
    args = parser.parse_args()

    main(args)
