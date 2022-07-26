import re

file_name = input("file name : ")

print(file_name)

class juniper:
    def __init__(self, data):
        self.data = data
    def network(self, data):
        re_addr = re.compile("ipaddr")
        data_addr = re_addr.search(data)
        return data_addr

    def service(self, data):
        re_service = re.compile("service")
        data_service = re_service.search(data)
        return data_service

    def manageip(self, data):
        re_manageip = re.compile("")