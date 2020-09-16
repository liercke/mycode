#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsfile:
    #dnslist = dnsfile.readlines()
    for svr in dnsfile:
        print(svr, end="")
