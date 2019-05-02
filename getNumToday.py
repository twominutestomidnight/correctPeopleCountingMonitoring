import requests
import datetime
from datetime import timedelta
from requests.auth import HTTPDigestAuth
from xml.dom import minidom
import re


def getTodayPeopleValue(ip, port, login, password, string):

    #url = 'http://192.168.30.50/ISAPI/System/Video/inputs/channels/1/counting/search/'
    url = 'http://{}:{}/ISAPI/System/Video/inputs/channels/1/counting/search/'.format(ip, port)
    #now = datetime.datetime.now()
    date_format = '%Y-%m-%d'
    today = datetime.datetime.now()
    today = today.strftime(date_format)
    #yesterday = today + timedelta(days=-1)
    #yesterday = yesterday.strftime(date_format)
    #print(yesterday)
    st = "{}-{}-{}".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)

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
    """.format(string, today, today)
    try:
        r = requests.get(url, auth=HTTPDigestAuth(login, password), data=payload, timeout = 5)


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
