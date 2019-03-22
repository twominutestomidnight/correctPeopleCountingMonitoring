import re

def parse_video(data):
    # information = dict()
    information = {}
    information['videoCodecType'] = re.findall(r'<videoCodecType>(.*?)<\/videoCodecType>', data)[0]
    videoResolutionWidth = re.findall(r'<videoResolutionWidth>(.*?)<\/videoResolutionWidth>', data)[0]
    videoResolutionHeight = re.findall(r'<videoResolutionHeight>(.*?)<\/videoResolutionHeight>', data)[0]
    information['Resolution'] = "{}*{}".format(videoResolutionWidth, videoResolutionHeight)
    try:
        information['constantBitRate'] = re.findall(r'<constantBitRate>(.*?)<\/constantBitRate>', data)[0]
    except:
        information['constantBitRate'] = 0
    information['maxFrameRate'] = re.findall(r'<maxFrameRate>(.*?)<\/maxFrameRate>', data)[0]
    if int(information['maxFrameRate'])==0:
        information['maxFrameRate'] = "full frame rate"
    return information
