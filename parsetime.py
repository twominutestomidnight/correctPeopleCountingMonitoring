import re
import time

def parse_time(data):
    # information = dict()
    information = {}
    timeMode = re.findall(r'<timeMode>(.*?)<\/timeMode>', data)[0]

    if timeMode == "NTP":
        information['NTP'] = 1
    else:
        information['NTP'] = 0


    information['localTime'] = re.findall(r'<localTime>(.*?)<\/localTime>', data)[0]

    information['timeZone'] = re.findall(r'<timeZone>(.*?)<\/timeZone>', data)[0]
    try:
        currentDSTsetting = re.findall(r'DST.*', information['timeZone'])[0]
        information['activateDST'] = 1
    except:
        currentDSTsetting = ""
        information['activateDST'] = 0

    #if information['timeZone'].find("DST") == -1:
        #information['activateDST'] = 0
    #else:
        #information['activateDST'] = 1

    #date_format = '%Y-%m-%dT'
    camera_time = re.findall(r'^[^+]*', information['localTime'])[0]
    local_time = time.time()

    information['diff_in_time'] = int(local_time) - int(time.mktime(time.strptime(camera_time, '%Y-%m-%dT%H:%M:%S')))
    ethalonDST = "DST01:00:00,M3.5.0/03:00:00,M10.5.0/04:00:00"
    if currentDSTsetting == ethalonDST:
        information['DSTsetting'] = 1
    else:
        information['DSTsetting'] = 0

    return information
