import requests
import datetime
from datetime import timedelta
from requests.auth import HTTPDigestAuth
from xml.dom import minidom
import re


def getStartPeopleValueMonthly(ip,port,login,password,string,str_start,str_finish):

    #url = 'http://192.168.30.50/ISAPI/System/Video/inputs/channels/1/counting/search/'
    url = 'http://{}:{}/ISAPI/System/Video/inputs/channels/1/counting/search/'.format(ip, port)



    payload = """
    <?xml version="1.0" encoding="utf-16"?>
    <countingStatisticsDescription
    	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    	xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    	<reportType>{}</reportType>
    	<timeSpanList>
    		<timeSpan>
    			<startTime>{}T00:00:00</startTime>
    			<endTime>{}T23:59:59</endTime>
    		</timeSpan>
    	</timeSpanList>
    </countingStatisticsDescription>
    """.format(string, str_start, str_finish)
    try:
        r = requests.get(url, auth=HTTPDigestAuth(login, password), data=payload)


        enterCount = re.findall(r'<enterCount>(.*?)<\/enterCount>',r.text )
        exitCount = re.findall(r'<exitCount>(.*?)<\/exitCount>',r.text )

        #print(enterCount)
        #print(exitCount)

        #itemlist = xmldoc.getElementsByTagName('enterCount')
        # for i in itemlist:
        #    print(i.firstChild.nodeValue)
        #day = datetime.datetime.today().weekday()
        #startEnterValue = (int)(itemlist[day].firstChild.nodeValue)
        # print("Len : ", itemlist)

        return enterCount, exitCount, "Online"
    except:
        return [], [], "Offline"
