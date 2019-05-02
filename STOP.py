import os
f = open('task_list.txt', 'r')
for line in f:
    #print(line)
    #os.system('schtasks.exe /query  /tn "{}"'.format(line))
    os.system('schtasks /delete /tn "{}" /f'.format(line))
f.close()
os.system('del task_list.txt')