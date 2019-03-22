from camera import Camera
import configparser
from DeviceInfo import deviceInfo
from read_xml import read_xml
from Time import deviceTime
from Video import deviceVideo
import time


if __name__ == '__main__':
    start_time = time.time()
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini')
    #print(config_ini['DEFAULT']['program_mode'])

    dict_list = read_xml(config_ini['DEFAULT']['read_file'])

    camerasArray = []

    for index in range(len(dict_list)):

        camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                   login=dict_list[index]['login'],password=dict_list[index]['password']))


    #result = open(config_ini['DEFAULT']['path_to_save_file'], "w", encoding='utf8')

    log = open(config_ini['DEFAULT']['log_file'], 'w')
    log.write("ip\tstatus_code_deviceInfo\tdeviceName\tdeviceID\tmodel\tserialNumber\tfirmwareVersion\t"
              "firmwareReleasedDate\tdeviceType\tstatus_code_time\tactivateDST\tDSTsetting\tlocalTime\tdiff_in_time\ttimeZone\tNTP\tstatus_code_video\tvideoCodecType\t"
              "Resolution\tconstantBitRate\tmaxFrameRate\n")
    for camer in camerasArray:
        print(camer)
        info_deviceInfo, status_code_deviceInfo = deviceInfo(camer.ip, camer.port, camer.login, camer.password)
        info_time, status_code_time = deviceTime(camer.ip, camer.port, camer.login, camer.password)
        info_video, status_code_video = deviceVideo(camer.ip, camer.port, camer.login, camer.password)
        log.write(camer.ip)
        if status_code_deviceInfo == 1:
            '''
            for key in info.keys():
                print(key)
                log.write("\t{}".format(key))
            log.write("\n")
            '''
            log.write("\t{}".format(status_code_deviceInfo))
            for values in info_deviceInfo.values():
                log.write("\t{}".format(values))

        if status_code_time == 1:
            log.write("\t{}".format(status_code_time))
            #for values in info_time.values():
                #log.write("\t{}".format(values))
            #print("{}{}{}".format(info_time['activateDST'],info_time['localTime'],info_time['timeZone']))
            log.write("\t{}\t{}\t{}\t{}\t{}\t{}".format(info_time['activateDST'],info_time['DSTsetting'], info_time['localTime'],
                                                info_time['diff_in_time'], info_time['timeZone'],
                                                        info_time['NTP']))

        if status_code_video == 1:
            log.write("\t{}".format(status_code_video))
            #for values in info_time.values():
                #log.write("\t{}".format(values))
            #print("{}-{}-{}".format(info_time['videoCodecType'],info_time['Resolution'],info_time['constantBitRate']))
            log.write("\t{}\t{}\t{}\t{}".format(info_video['videoCodecType'],info_video['Resolution'],
                                                info_video['constantBitRate'],info_video['maxFrameRate']))


        if status_code_deviceInfo == -1:
            log.write("\t{}\tError while connection".format(status_code_deviceInfo))
        '''    
        if status_code_time == -1:
            log.write("\t{}".format(status_code_time))

        if status_code_video == -1:
            log.write("\t{}".format(status_code_video))
            
        '''

        log.write("\n")
    print("--- %.5s seconds ---" % (time.time() - start_time))