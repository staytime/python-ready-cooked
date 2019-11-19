#! /usr/bin/python3

# properse:
# 1. demo encoding string to writing as binary
# 2. demo cross plaform EOL charactor using \n



from pathlib import Path
import os
import datetime



dump_foramt = '=' * 64 + '\n' \
                  + 'dump @ {}\n' \
                  + '=' * 64 + '\n' \
                  + '{}\n' \
                  + '=' * 64 + '\n'



def write(path, payload):
    t = datetime.datetime.now()
    __ = dump_foramt.format(t.strftime('%Y%m%d %R:%S'), \
                            payload)
    
    with open(path, 'wb') as f:
        f.write(__.encode('utf-8'))
    
