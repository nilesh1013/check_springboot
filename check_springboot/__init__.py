#!/usr/bin/env python
import requests
import sys
import argparse


def info():
    print ("A Nagios plugin for checking springboot service using API")


def check_springboot_service():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port")
    parser.add_argument("--host")
    args = parser.parse_args()

    try:
        resp = requests.get('http://{0}:{1}/health'.format(args.host, args.port), timeout=2.0).json()
    except:
        print ("FAIL!")
        sys.exit(2)

    if resp['status'] == 'UP':
        print ("OK")
        sys.exit(0)
    else:
        print ("FAIL!")
        sys.exit(2)

