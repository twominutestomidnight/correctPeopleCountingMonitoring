from xml.etree import ElementTree as ET
import configparser
import os
config_ini = configparser.ConfigParser()
config_ini.read('config.ini')

os.system("mkdir {}\\today".format(config_ini['DEFAULT']['path_to_save_file']))
print(config_ini['DEFAULT']['time'])
time_periods = config_ini['DEFAULT']['time'].split(',')
print('======')
core_xml = '''
<?xml version="1.0" encoding="UTF-16"?>
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
'''.format('435', '245', '244')

#print(core_xml)




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
    os.system("del res.xml")



for time in time_periods:
    program(time,config_ini['DEFAULT']['path_to_exe_file'],
            config_ini['DEFAULT']['path_to_working_directory_file'])

#changeHeader('eww.xml')

'''
changeParametersXML('daily.xml', 1)
changeHeader('new_daily.xml')
changeParametersXML('weekly.xml', 2)
changeHeader('new_weekly.xml')
changeParametersXML('monthly.xml', 3)
changeHeader('new_monthly.xml')


os.system('schtasks /create /xml n_new_daily.xml /tn "dailyTask"')
os.system('schtasks /create /xml n_new_weekly.xml /tn "weeklyTask"')
os.system('schtasks /create /xml n_new_monthly.xml /tn "monthlyTask"')


os.system("del new_daily.xml")
os.system("del new_weekly.xml")
os.system("del new_monthly.xml")
os.system("del n_new_daily.xml")
os.system("del n_new_weekly.xml")
os.system("del n_new_monthly.xml")
'''