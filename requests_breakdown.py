#! /usr/bin/python3

"""
Purpose:
1. demo requests module time usage property

see also 
https://2.python-requests.org/en/master/api/#requests.Response.elapsed

"""



import requests






def request_get_response_time():
    # thx google
    url = 'http://www.google.com.tw'

    # send get request here, but all method are the same
    response = requests.get('http://www.google.com.tw', \
                            timeout = 30)

    print('response code = {}'.format(response.status_code))
    print('elapsed object type = {}'.format(type(response.elapsed)))
    print('time cost = {}s'.format(response.elapsed.total_seconds()))


    
if __name__ == '__main__':
    request_get_response_time()
