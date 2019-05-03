import os
import subprocess
f = open('task_list.txt', 'r')
for line in f:
    line = line.split('\n')[0]
    #print(line)
    #os.system('schtasks.exe /query  /tn "{}"'.format(line))
    #os.system('schtasks /delete /tn {} /f'.format(line))
    str = 'schtasks /delete /tn "{}" /f'.format(line)
    subprocess.run(str)
f.close()
os.system('del task_list.txt')