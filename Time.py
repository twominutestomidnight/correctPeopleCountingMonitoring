import requests
from requests.auth import HTTPDigestAuth
from parsetime import parse_time

def deviceTime(ip,port,login,password):
    url = 'http://{}:{}/ISAPI/System/time'.format(ip, port)
    #print(url)
    try:
        r = requests.get(url, auth=HTTPDigestAuth(login, password))
        #print(r.text)
        w = parse_time(r.text)
        return w, 1
    except:
        return "Error", -1
