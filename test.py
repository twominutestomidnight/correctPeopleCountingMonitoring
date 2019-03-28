from xml.etree import ElementTree as ET
import re
import configparser
import os
config_ini = configparser.ConfigParser()
config_ini.read('config.ini')


'''
tree = et.parse('daily.xml')
#tree.find('idinfo/timeperd/timeinfo/rngdates/begdate').text = '1/1/2011'
#tree.find('Task/Actions/Exec/WorkingDirectory').text = '1/1/2011'
tree.find('.//WorkingDirectory') = '1/1/2011'
tree.write('daily.xml')

'''
'''
tree = ET.parse('example.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)

arr =tree.findall('country/rank')
for a in arr:
    a.text += "q"

tree.write('example2.xml')



#it works !
tree = ET.parse('daily.xml')
root = tree.getroot()
#for child in root:
    #print(child.tag, child.attrib)

arr = tree.findall('Actions/Exec/Command')
arr[0].text = config_ini['DEFAULT']['path_to_save_file']

tree.write('new_daily.xml')
'''

def changeParametersXML(xml,arg):
    tree = ET.parse(xml)
    root = tree.getroot()
    # for child in root:
    # print(child.tag, child.attrib)
    print(root.tag)
    arr = tree.findall('Actions/Exec/WorkingDirectory')
    #print(arr[0].text)
    arr[0].text = config_ini['DEFAULT']['path_to_working_directory_file']


    arr2 = tree.findall('Actions/Exec/Command')
    arr2[0].text = config_ini['DEFAULT']['path_to_exe_file']

    arr3 = tree.findall('Actions/Exec/Arguments')
    arr3[0].text = str(arg)


    tree.write('new_'+ xml)


def changeHeader(xml):
    with open('new_daily.xml',"r+") as f:
        data = f.read()
        #f.close()
        #print(data)
    data = data.replace('<Task version="1.2">','<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">')
    tree = open("n_"+xml, "w")
    tree.write(data)
changeParametersXML('daily.xml', 1)
changeHeader('new_daily.xml')
changeParametersXML('weekly.xml', 2)
changeHeader('new_weekly.xml')
changeParametersXML('monthly.xml', 3)
changeHeader('new_monthly.xml')


os.system('schtasks /create /xml n_new_daily.xml /tn "MyTask111"')
os.system('schtasks /create /xml n_new_weekly.xml /tn "MyTask222"')
os.system('schtasks /create /xml n_new_monthly.xml /tn "MyTask333"')




