#!/usr/bin/env python
import urllib

import socks
import socket

import sys, getopt


def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock


socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)

socket.socket = socks.socksocket
socket.create_connection = create_connection

import urllib2

URL = "http://pwndb2am4tzkvold.onion/"
USER = '[luser] => '
DOMAIN = '[domain] => '
PASSWORD = '[password] => '


def main(argv):
    user = '%'
    domain = '%'
    try:
        opts, args = getopt.getopt(argv, "hu:d:", ["username=", "domain="])
    except getopt.GetoptError:
        print 'pwndb.py -u <username> -d <domain>'
        sys.exit(2)
    if not opts:
        print 'pwndb.py -u <username> -d <domain>'
        sys.exit(-1)

    for opt, arg in opts:
        if opt == '-h':
            print 'pwndb.py -u <username> -d <domain>'
            sys.exit(-1)
        elif opt in ("-u", "--username"):
            user = "{}{}".format(arg, user)
        elif opt in ("-d", "--domain"):
            domain = "{}{}".format(arg, domain)

    print "Searching...\n"

    data = {'luser': "{}".format(user),
            'domain': "{}".format(domain),
            'luseropr': 1, 'domainopr': 1,
            'submitform': 'em'}


    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    data = urllib.urlencode(data)
    request = urllib2.Request(URL, data=data)
    request.add_header("Content-Type", 'application/x-www-form-urlencoded')
    request.get_method = lambda: "POST"

    try:
        connection = opener.open(request)
    except urllib2.HTTPError, e:
        connection = e

    if connection.code != 200:
        print "ERROR: Unable to connect."
        sys.exit(1)

    response = connection.read()
    results = [i for i in range(len(response)) if response.startswith(USER, i)]

    for position in range(len(results)):
        init = len(USER) + results[position]

        first_slice = response[init:]
        username = response[init:init + first_slice.find("\n")]
        init = first_slice.find(DOMAIN) + len(DOMAIN)
        second_slice = first_slice[init:]
        domain = first_slice[init: init + second_slice.find("\n")]
        init = second_slice.find(PASSWORD) + len(PASSWORD)
        third_slice = second_slice[init:]
        password = second_slice[init: init + third_slice.find("\n")]

        print "\t{}@{} : {}".format(username, domain, password)

    print "\nDone."

if __name__ == '__main__':
    print '''
                          _ _     
                         | | |    
  _ ____      ___ __   __| | |__  
 | '_ \ \ /\ / / '_ \ / _` | '_ \ 
 | |_) \ V  V /| | | | (_| | |_) |
 | .__/ \_/\_/ |_| |_|\__,_|_.__/ 
 | |                              
 |_|                              
 
    '''
    main(sys.argv[1:])
