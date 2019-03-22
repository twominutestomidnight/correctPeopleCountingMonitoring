from os import mkdir, system
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini')
#print(config_ini['DEFAULT']['path_to_save_file'])
mkdir("daily")
mkdir("weekly")
mkdir("monthly")
system('SchTasks /Create /SC DAILY /TN "daily" /TR "{}/app.exe" 1 /ST 00:02'.format(config_ini['DEFAULT']['path_to_save_file']))
system('SchTasks /Create /SC WEEKLY /D MON /TN "weekly" /TR "{}/app.exe 2" /ST 00:02'.format(config_ini['DEFAULT']['path_to_save_file']))
system('SchTasks /Create /SC MONTHLY /D 1 /TN "monthly" /TR "{}/app.exe 3" /ST 00:02'.format(config_ini['DEFAULT']['path_to_save_file']))

#path_to_save_log = config_ini['DEFAULT']['path_to_save_log']
#completeName = "123.txt"
#try:
#   os.mkdir("daily")
#except:
#    print("error")