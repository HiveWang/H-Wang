# coding:utf-8

import optparse
import socket
from socket import *

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print('tcp open {}'.format(tgtHost))
        print('[+] '+str(results))
        connSkt.close()
    except:
        print('[-]{} tcp close'.format(tgtPort))


def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Connot resolve {} : Unkown host'.format(tgtHost))
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('Scan Results for:{}'.format(tgtName[0]))
    except:
        print('Scan Results for:{}'.format(tgtIP))
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port:{}'.format(tgtPort))
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser("usage%prog -H <target host> -P <target port>")
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgtPort', type='string', help='specify target port')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts == None):
        print('You must specify a target host and a target port')
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()