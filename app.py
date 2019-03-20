from getCamNum import getStartPeopleValue
import datetime
from datetime import timedelta
from xlrd import open_workbook
from camera import Camera
import os.path
import configparser
from getNumWeekly import getStartPeopleValueWeekly
from getNumMonthly import getStartPeopleValueMonthly
import calendar
import datetime
import sys

if __name__ == '__main__':
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini')
    #print(config_ini['DEFAULT']['program_mode'])
    try:
        print('Number of arguments:', len(sys.argv), 'arguments.')
        print('Argument List:', str(sys.argv))
        program_mode = int(sys.argv[1])
        print("program_mode", program_mode)
    except:
        program_mode = 1

    if program_mode == 1:

        #df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        #df = read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        print("trying read file with input data")
        '''
        it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
        for x in range(6):
            time.sleep(.3)  # выполнение функции
            print(next(it), end='', flush=True)
        '''
        #df = read_excel(config_ini['DEFAULT']['read_file'], index = ['ip', 'port', 'login', 'password','name'],
        #                encoding='sys.getfilesystemencoding()')
        book = open_workbook(config_ini['DEFAULT']['read_file'], 'utf-8')
        sheet = book.sheet_by_index(0)
        dict_list = []
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)

        #print(dict_list[0])
        #print(type(dict_list))

        print('Reading to file was successful.')
        #print(df)

        camerasArray = []

        for index in range(len(dict_list)):

            camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                       login=dict_list[index]['login'],password=dict_list[index]['password'],
                                       desc=dict_list[index]['name']))

        save_path = config_ini['DEFAULT']['path_to_save_file']
        #dtime = datetime.datetime.strptime("{}", "%y-%m-%d-H-%M")
        if datetime.datetime.now().month<10:
            month = "0"+str(datetime.datetime.now().month)
        else:
            month = str(datetime.datetime.now().month)


        if int(datetime.datetime.now().day)<10:
            day = "0"+str(datetime.datetime.now().day)
        else:
            day = str(datetime.datetime.now().day)

        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)


        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)

        if int(datetime.datetime.now().minute) < 10:
            minute = "0" + str(datetime.datetime.now().minute)
        else:
            minute = str(datetime.datetime.now().minute)
        #print(datetime.datetime.now().day)
        if int(datetime.datetime.now().second) < 10:
            second = "0" + str(datetime.datetime.now().second)
        else:
            second = str(datetime.datetime.now().second)
        #print(datetime.datetime.now().day)

        stri = "{}-{}-{}-{}-{}-{}-daily.csv".format(datetime.datetime.now().year,month,
                                       day,hour,minute,second)


        completeName = os.path.join(save_path, stri)
        result = open(completeName, "w", encoding='utf8')
        #date_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        today = datetime.datetime.now()
        yesterday = today + timedelta(days=-1)
        yesterday = yesterday.strftime(date_format)
        #result.write("{}-{}-{} \n".format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        result.write(str(yesterday)+"\t\t\t\t00:00-01:00\t01:00-02:00\t02:00-03:00\t03:00-04:00\t04:00-05:00\t05:00-06:00\t"
                     "06:00-07:00\t07:00-08:00\t08:00-09:00\t09:00-10:00\t10:00-11:00\t"
                     "11:00-12:00\t12:00-13:00\t13:00-14:00\t14:00-15:00\t15:00-16:00\t16:00-17:00\t17:00-18:00\t"
                     "18:00-19:00\t19:00-20:00\t20:00-21:00\t21:00-22:00\t22:00-23:00\t23:00-24:00\n")
        #result.write(str(datetime.datetime.now())+"\n")
        result.write("""IP\tName\tDirections\tStatus\n""")
        print(len(camerasArray))
        i = 1

        for camer in camerasArray:
            print("start work with camera, ip : {}".format(camer.ip))
            '''
            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(6):
                time.sleep(.3)  # выполнение функции
                print(next(it), end='', flush=True)
            '''

            string = 'daily'
            # enter, exit = getStartPeopleValue()
            enter, exit, status = getStartPeopleValue(camer.ip, camer.port, camer.login, camer.password, string)

            #print(enter)
            #print(exit)
            #print(status)
            #print(camer.desc)
            #print(type(camer.desc))    #= camer.desc.replace("'", "''")
            #camer.desc = camer.desc.replace('"', '""')
            #result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))
            result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))

            result.write('\t\tEnter')
            result.write("\t\t")
            for i in range(len(enter)):
                

                result.write(enter[i] + "\t")
            result.write('\n')
            result.write('\t\tExit')
            result.write("\t\t")
            for i in range(len(enter)):
                
                result.write(exit[i] + "\t")
            result.write('\n')


                #printRes(st,enter, exit)

            print('finish work with this camera.')
        #print(end_date)
        #print("Next report will be create in : " + end_date)

        result.close()
        print("Today report : " +str(datetime.datetime.now()))

    if program_mode == 2:

        # df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        # df = read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        print("trying read file with input data")
        '''
        it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
        for x in range(6):
            time.sleep(.3)  # выполнение функции
            print(next(it), end='', flush=True)
        '''
        # df = read_excel(config_ini['DEFAULT']['read_file'], index = ['ip', 'port', 'login', 'password','name'],
        #                encoding='sys.getfilesystemencoding()')
        book = open_workbook(config_ini['DEFAULT']['read_file'], 'utf-8')
        sheet = book.sheet_by_index(0)
        dict_list = []
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)

        # print(dict_list[0])
        # print(type(dict_list))

        print('Reading to file was successful.')
        # print(df)

        camerasArray = []

        for index in range(len(dict_list)):
            camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                       login=dict_list[index]['login'], password=dict_list[index]['password'],
                                       desc=dict_list[index]['name']))

        save_path = config_ini['DEFAULT']['path_to_save_file']
        # dtime = datetime.datetime.strptime("{}", "%y-%m-%d-H-%M")
        if datetime.datetime.now().month < 10:
            month = "0" + str(datetime.datetime.now().month)
        else:
            month = str(datetime.datetime.now().month)

        if int(datetime.datetime.now().day) < 10:
            day = "0" + str(datetime.datetime.now().day)
        else:
            day = str(datetime.datetime.now().day)

        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)

        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)

        if int(datetime.datetime.now().minute) < 10:
            minute = "0" + str(datetime.datetime.now().minute)
        else:
            minute = str(datetime.datetime.now().minute)
        # print(datetime.datetime.now().day)
        if int(datetime.datetime.now().second) < 10:
            second = "0" + str(datetime.datetime.now().second)
        else:
            second = str(datetime.datetime.now().second)
        # print(datetime.datetime.now().day)

        stri = "{}-{}-{}-{}-{}-{}-weekly.csv".format(datetime.datetime.now().year, month,
                                              day, hour, minute, second)

        completeName = os.path.join(save_path, stri)
        result = open(completeName, "w", encoding='utf8')
        # date_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        #today = datetime.datetime.now()
        today = datetime.datetime.now().date() - timedelta(days=7)
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)

        Monday = start
        Tuesday = (start + timedelta(days=1)).strftime(date_format)
        Wednesday = (start + timedelta(days=2)).strftime(date_format)
        Thursday = (start + timedelta(days=3)).strftime(date_format)
        Friday = (start + timedelta(days=4)).strftime(date_format)
        Saturday = (start + timedelta(days=5)).strftime(date_format)
        Sunday = (start + timedelta(days=6)).strftime(date_format)


        start = start.strftime(date_format)
        end = end.strftime(date_format)
        '''
        print("Today: " + str(today))
        print("Start: " + str(start))
        print("End: " + str(end))
        '''
        result.write(
            str(start) + " " + str(end) + "\t\t\t\t{}\t{}\t{}\t{}\t{}\t{}\t"
                             "{}\n".format(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday))
        # result.write(str(datetime.datetime.now())+"\n")
        result.write("""IP\tName\tDirections\tStatus\n""")
        print(len(camerasArray))
        i = 1
        for camer in camerasArray:
            print("start work with camera, ip : {}".format(camer.ip))
            '''
            it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
            for x in range(6):
                time.sleep(.3)  # выполнение функции
                print(next(it), end='', flush=True)
            '''
            string = 'weekly'
            # enter, exit = getStartPeopleValue()
            enter, exit, status = getStartPeopleValueWeekly(camer.ip, camer.port, camer.login, camer.password, string)

            # print(enter)
            # print(exit)
            # print(status)
            # print(camer.desc)
            # print(type(camer.desc))    #= camer.desc.replace("'", "''")
            # camer.desc = camer.desc.replace('"', '""')
            # result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))
            result.write(u"{}\t{}\t\t{}\n".format(camer.ip, camer.desc, status))

            result.write('\t\tEnter')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(enter[i] + "\t")
            result.write('\n')
            result.write('\t\tExit')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(exit[i] + "\t")
            result.write('\n')

            # printRes(st,enter, exit)

            print('finish work with this camera.')
        # print(end_date)
        # print("Next report will be create in : " + end_date)

        result.close()
        print("Today report : " + str(datetime.datetime.now()))



    if program_mode == 3:

        # df = pandas.read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        # df = read_excel('names.xls', index = ['ip', 'port', 'login', 'password','name'])
        print("trying read file with input data")
        '''
        it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
        for x in range(6):
            time.sleep(.3)  # выполнение функции
            print(next(it), end='', flush=True)
        '''
        # df = read_excel(config_ini['DEFAULT']['read_file'], index = ['ip', 'port', 'login', 'password','name'],
        #                encoding='sys.getfilesystemencoding()')
        book = open_workbook(config_ini['DEFAULT']['read_file'], 'utf-8')
        sheet = book.sheet_by_index(0)
        dict_list = []
        keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)

        # print(dict_list[0])
        # print(type(dict_list))

        print('Reading to file was successful.')
        # print(df)

        camerasArray = []

        for index in range(len(dict_list)):
            camerasArray.append(Camera(ip=dict_list[index]['ip'], port=int(dict_list[index]['port']),
                                       login=dict_list[index]['login'], password=dict_list[index]['password'],
                                       desc=dict_list[index]['name']))

        save_path = config_ini['DEFAULT']['path_to_save_file']
        # dtime = datetime.datetime.strptime("{}", "%y-%m-%d-H-%M")
        if datetime.datetime.now().month < 10:
            month = "0" + str(datetime.datetime.now().month)
        else:
            month = str(datetime.datetime.now().month)

        if int(datetime.datetime.now().day) < 10:
            day = "0" + str(datetime.datetime.now().day)
        else:
            day = str(datetime.datetime.now().day)

        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)

        if int(datetime.datetime.now().hour) < 10:
            hour = "0" + str(datetime.datetime.now().hour)
        else:
            hour = str(datetime.datetime.now().hour)

        if int(datetime.datetime.now().minute) < 10:
            minute = "0" + str(datetime.datetime.now().minute)
        else:
            minute = str(datetime.datetime.now().minute)
        # print(datetime.datetime.now().day)
        if int(datetime.datetime.now().second) < 10:
            second = "0" + str(datetime.datetime.now().second)
        else:
            second = str(datetime.datetime.now().second)
        # print(datetime.datetime.now().day)

        stri = "{}-{}-{}-{}-{}-{}-monthly.csv".format(datetime.datetime.now().year, month,
                                              day, hour, minute, second)

        completeName = os.path.join(save_path, stri)
        result = open(completeName, "w", encoding='utf8')
        # date_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        #today = datetime.datetime.now()
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        if lastMonth.month < 10:
            m = "0" + str(lastMonth.month)
        else:
            m = str(lastMonth.month)
        print(calendar.monthrange(lastMonth.year, lastMonth.month)[1])
        #print(lastMonth.year,lastMonth.month)

        s = "{}-{}".format(lastMonth.year, m)
        result.write(s + "\t\t\t\t")
        first_day = "01"
        last_day = calendar.monthrange(lastMonth.year, lastMonth.month)[1]
        print("lastMonth: ",lastMonth.year, lastMonth.month)

        str_start = "{}-{}-{}".format(lastMonth.year,m,first_day)
        str_finish = "{}-{}-{}".format(lastMonth.year,m,last_day)
        print("lastM: ", str_start, str_finish)
        for ind in range(1,calendar.monthrange(lastMonth.year, lastMonth.month)[1]+1):
            if ind < 10:
                ind = "0" + str(ind)
            print(ind)
            result.write(str(ind) + "\t")
        result.write("\n")

        result.write("""IP\tName\tDirections\tStatus\n""")
        print(len(camerasArray))
        i = 1

        for camer in camerasArray:
            print(camer)
            string = 'monthly'
            enter, exit, status = getStartPeopleValueMonthly(camer.ip, camer.port, camer.login, camer.password, string, str_start, str_finish)
            #enter, exit, status = getStartPeopleValueMonthly(camer.ip, camer.port, camer.login, camer.password, string, "2019-03-01", "2019-03-31")

            result.write(u"{}\t{}\t\t{}\n".format(camer.ip, camer.desc, status))

            result.write('\t\tEnter')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(enter[i] + "\t")
            result.write('\n')
            result.write('\t\tExit')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(exit[i] + "\t")
            result.write('\n')


            #print('finish work with this camera.')


        result.close()
        print("Today report : " + str(datetime.datetime.now()))






        '''

        start = start.strftime(date_format)
        end = end.strftime(date_format)

        print("Today: " + str(today))
        print("Start: " + str(start))
        print("End: " + str(end))
        
        result.write(
            str(start)+" "+ str(end) + "\t\t\t\t{}\t{}\t{}\t{}\t{}\t{}\t"
                             "{}\n".format(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday))
        # result.write(str(datetime.datetime.now())+"\n")
        result.write("""IP\tName\tDirections\tStatus\n""")
        print(len(camerasArray))
        i = 1
        for camer in camerasArray:
            print("start work with camera, ip : {}".format(camer.ip))
            
            string = 'weekly'
            # enter, exit = getStartPeopleValue()
            enter, exit, status = getStartPeopleValueWeekly(camer.ip, camer.port, camer.login, camer.password, string)

            # print(enter)
            # print(exit)
            # print(status)
            # print(camer.desc)
            # print(type(camer.desc))    #= camer.desc.replace("'", "''")
            # camer.desc = camer.desc.replace('"', '""')
            # result.write(u"{}\t{}\t\t{}\n".format(camer.ip,camer.desc,status))
            result.write(u"{}\t{}\t\t{}\n".format(camer.ip, camer.desc, status))

            result.write('\t\tEnter')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(enter[i] + "\t")
            result.write('\n')
            result.write('\t\tExit')
            result.write("\t\t")
            for i in range(len(enter)):
                result.write(exit[i] + "\t")
            result.write('\n')

            # printRes(st,enter, exit)

            print('finish work with this camera.')
        # print(end_date)
        # print("Next report will be create in : " + end_date)

        result.close()
        print("Today report : " + str(datetime.datetime.now()))
        '''

