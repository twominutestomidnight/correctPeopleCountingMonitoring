from xml.etree import ElementTree as ET
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
os.system("mkdir {}\daily".format(config_ini['DEFAULT']['path_to_save_file']))
os.system("mkdir {}\weekly".format(config_ini['DEFAULT']['path_to_save_file']))
os.system("mkdir {}\monthly".format(config_ini['DEFAULT']['path_to_save_file']))
os.system("mkdir {}\\today".format(config_ini['DEFAULT']['path_to_save_file']))


def changeParametersXML(xml,arg):
    tree = ET.parse(xml)
    root = tree.getroot()
    # for child in root:
    # print(child.tag, child.attrib)
    #print(root.tag)
    arr = tree.findall('Actions/Exec/WorkingDirectory')
    #print(arr[0].text)
    arr[0].text = config_ini['DEFAULT']['path_to_working_directory_file']


    arr2 = tree.findall('Actions/Exec/Command')
    arr2[0].text = config_ini['DEFAULT']['path_to_exe_file']

    arr3 = tree.findall('Actions/Exec/Arguments')
    arr3[0].text = str(arg)

    tree.write('new_' + xml)


def changeHeader(xml):
    with open(xml, "r+") as f:
        data = f.read()
        #f.close()
        #print(data)
    data = data.replace('<Task version="1.2">', '<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">')
    tree = open("n_"+xml, "w")
    tree.write(data)

changeParametersXML('daily.xml', 1)
changeHeader('new_daily.xml')
changeParametersXML('weekly.xml', 2)
changeHeader('new_weekly.xml')
changeParametersXML('monthly.xml', 3)
changeHeader('new_monthly.xml')

f1 = open('task_list.txt','w')
os.system('schtasks /create /xml n_new_daily.xml /tn "dailyTask"')
f1.write('dailyTask\n')
os.system('schtasks /create /xml n_new_weekly.xml /tn "weeklyTask"')
f1.write('weeklyTask\n')
os.system('schtasks /create /xml n_new_monthly.xml /tn "monthlyTask"')
f1.write('monthlyTask\n')


os.system("del new_daily.xml")
os.system("del new_weekly.xml")
os.system("del new_monthly.xml")
os.system("del n_new_daily.xml")
os.system("del n_new_weekly.xml")
os.system("del n_new_monthly.xml")





os.system("mkdir {}\\today".format(config_ini['DEFAULT']['path_to_save_file']))
time_periods = config_ini['DEFAULT']['time'].split(',')





def program(time_period,path_exe,working_directory):

    core_xml = '''<?xml version="1.0" encoding="UTF-16"?>
    <Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
      <Triggers>
        <CalendarTrigger>
          <StartBoundary>2019-05-02T{}:00</StartBoundary>
          <Enabled>true</Enabled>
          <ScheduleByDay>
            <DaysInterval>1</DaysInterval>
          </ScheduleByDay>
        </CalendarTrigger>
      </Triggers>

      <Settings>
        <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
        <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
        <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
        <AllowHardTerminate>true</AllowHardTerminate>
        <StartWhenAvailable>false</StartWhenAvailable>
        <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
        <IdleSettings>
          <StopOnIdleEnd>true</StopOnIdleEnd>
          <RestartOnIdle>false</RestartOnIdle>
        </IdleSettings>
        <AllowStartOnDemand>true</AllowStartOnDemand>
        <Enabled>true</Enabled>
        <Hidden>false</Hidden>
        <RunOnlyIfIdle>false</RunOnlyIfIdle>
        <WakeToRun>false</WakeToRun>
        <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
        <Priority>7</Priority>
      </Settings>
      <Actions Context="Author">
        <Exec>
          <Command>{}</Command>
          <Arguments>4</Arguments>
          <WorkingDirectory>{}</WorkingDirectory>
        </Exec>
      </Actions>
    </Task>
    '''.format(time_period, path_exe, working_directory)
    f = open('res.xml', 'w')
    f.write(core_xml)
    f.close()
    os.system('schtasks /create /xml res.xml /tn "{}"'.format(time_period.split(':')[0]))
    f1.write('{}\n'.format(format(time_period.split(':')[0])))
    os.system("del res.xml")




for time in time_periods:
    program(time, config_ini['DEFAULT']['path_to_exe_file'],
            config_ini['DEFAULT']['path_to_working_directory_file'])
f1.close()