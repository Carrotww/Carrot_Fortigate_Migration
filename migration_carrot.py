import re
import os
import time
from typing import List
import collections

if __name__ == '__main__':
    class juniper:
        def __init__(self):
            pass

        def trans_addr(self, line, file_path, new_file_name) -> List:
            # new_file = open(f'C:\\Users\\K1220006\\Desktop\\{new_file_name}.txt', 'w')
            path = file_path + new_file_name
            new_file = open(f'{path}.txt', 'w')
            fgt_addr = [i.split() for i in line if "set address" in i]
            result = []
            for line in fgt_addr:
                s_result = []
                i = 0
                while i < len(line):
                    temp_str = line[i]
                    if line[i][0] == '"' and line[i][-1] != '"':
                        i += 1
                        while line[i][-1] != '"':
                            temp_str += line[i]
                            i += 1
                        temp_str += line[i]
                    i += 1
                    s_result.append(temp_str)
                result.append(s_result)

            new_file.write('config firewall address\n')
            ip_match = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

            for i in result:
                # print('config firewall address', '\n','edit name {0}'.format(i[3]), '\n\t',
                #       'set subnet {0} {1}'.format(i[4], i[5]), '\n', 'next')
                #  #  프린트 하는 부분
                if re.match(ip_match, i[4]):
                    new_file.write(f'edit {i[3]}\nset subnet {i[4]} {i[5]}\nnext\n')
                else:
                    new_file.write(f'edit {i[3]}\nset type fqdn\nset fqdn {i[4]}\nnext\n')
            new_file.write('\n')
            new_file.close()

            return new_file

        def trans_addrgrp(self, line, file_path, new_file_name) -> List:
            # new_file = open(f'C:\\Users\\K1220006\\Desktop\\{new_file_name}.txt', 'w')
            path = file_path + new_file_name
            new_file = open(f'{path}.txt', 'w')

            temp_addrgrp = [i.split() for i in line if "set group address" in i]
            result = []
            for line in temp_addrgrp:
                s_result = []
                i = 0
                while i < len(line):
                    temp_str = line[i]
                    if line[i][0] == '"' and line[i][-1] != '"':
                        i += 1
                        while line[i][-1] != '"':
                            temp_str += line[i]
                            i += 1
                        temp_str += line[i]
                    i += 1
                    s_result.append(temp_str)
                result.append(s_result)
            fgt_addrgrp = collections.defaultdict(list)

            new_file.write('config firewall addrgrp\n')
            for temp in result:
                if len(temp) == 7 and temp[5] == 'add':
                    fgt_addrgrp[temp[4]].append(temp[6])
            for key, val in fgt_addrgrp.items():
                new_file.write(f'edit {key}\nset member ')
                for mem in val:
                    new_file.write(f'{mem} ')
                new_file.write('\nnext\n')
            new_file.close()

            return new_file

        def trans_service(self, line) -> List:
            re_service = re.compile("service")
            data_service = re_service.search(line)
            return data_service

        def trans_manageip(self, line) -> List:
            re_manageip = re.compile("")

    def findfile(name, path): # 파일 이름으로 경로 찾는 func
        start = time.time()
        for dirpath, dirname, filename in os.walk(path):
            cur_time = time.time()
            if name in filename:
                return os.path.join(dirpath, name)
            elif cur_time >= (start + 10):
                return "파일명을 다시 확인해 주세요 - hyeongseok"

    config_file_name = input("Enter the file name : ") # File path input line
    file_full_path = findfile(f"{config_file_name}", "C:\\") # config file path
    file_path = file_full_path.split(config_file_name)[0]
    file = open(f'{file_full_path}', 'r')

    # file = open('C:\\Users\\K1220006\\Desktop\\위비스 config.txt', 'r') # home desktop file path

    line = file.readlines() # line = file을 읽어와 한 줄 씩 부여줌
    jun = juniper() # import juniper class juniper
    fgt_addr_filename = input(f"Enter the {config_file_name} addr_filename : ")
    fgt_addrgrp_filename = input(f"Enter the {config_file_name} addrgrp_filename : ")

    fgt_addr = jun.trans_addr(line, file_path, fgt_addr_filename)
    fgt_addrgrp = jun.trans_addrgrp(line, file_path, fgt_addrgrp_filename)
    # print(fgt_addrgrp)
    # print(fgt_addr)

    file.close()