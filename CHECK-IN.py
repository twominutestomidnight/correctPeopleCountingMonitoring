import os
import sys
import configparser

if __name__ == '__main__':

    f = open('task_list.txt', 'r')
    for line in f:
        #print(line)
        os.system('schtasks.exe /query  /tn "{}"'.format(line))




    sys.stdin.read(1)



