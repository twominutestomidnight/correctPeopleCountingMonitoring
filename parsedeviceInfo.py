import re

def parse_deviceInfo(data):

    #information = dict()
    information = {}

    information['deviceName'] = re.findall(r'<deviceName>(.*?)<\/deviceName>', data)[0]

    information['deviceID'] = re.findall(r'<deviceID>(.*?)<\/deviceID>', data)[0]

    information['model'] = re.findall(r'<model>(.*?)<\/model>', data)[0]

    information['serialNumber'] = re.findall(r'<serialNumber>(.*?)<\/serialNumber>', data)[0]
    
    information['firmwareVersion'] = re.findall(r'<firmwareVersion>(.*?)<\/firmwareVersion>', data)[0]

    information['firmwareReleasedDate'] = re.findall(r'<firmwareReleasedDate>(.*?)<\/firmwareReleasedDate>', data)[0]

    information['deviceType'] = re.findall(r'<deviceType>(.*?)<\/deviceType>', data)[0]

    return information



