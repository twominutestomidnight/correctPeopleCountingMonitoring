class Camera:
    def __init__(self,ip,port,login,password,desc):
        self.ip = ip
        self.port = port
        self.login = login
        self.password = password
        self.desc = desc


    def __str__(self):
        return "ip : " + self.ip + ", port : " + str(self.port) + ", login : " + self.login + ", password : " \
               + self.password + ", desc : " + self.desc