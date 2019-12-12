#! /usr/bin/python3




import os


print(os.linesep)

with open('test-log.log', 'wb') as f:
    for i in range(10):
        __ = 'TESTING LOG'
        f.write(__.encode('utf-8'))
        f.write('\r\n'.encode('utf-8'))

