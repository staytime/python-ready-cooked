#! /usr/bin/python3
# 
# Properse:
# get datetime from string by using strptime
# get last second of date by using datetimt.time.max



import datetime



record_time = datetime.datetime.\
              strptime('2019-11-19 00:31:44', \
                       '%Y-%m-%d %H:%M:%S')

print(record_time)


# get to last second of day
record_time = datetime.datetime.combine(record_time.date(), \
                                        datetime.time.max)

print(record_time)



