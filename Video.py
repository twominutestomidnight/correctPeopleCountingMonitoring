import requests
from requests.auth import HTTPDigestAuth
from parsevideo import parse_video

def deviceVideo(ip,port,login,password):
    url = 'http://{}:{}/ISAPI/Streaming/channels/101'.format(ip, port)
    #print(url)
    try:
        r = requests.get(url, auth=HTTPDigestAuth(login, password))
        #print(r.text)
        w = parse_video(r.text)
        return w, 1
    except:
        return "Error", -1
