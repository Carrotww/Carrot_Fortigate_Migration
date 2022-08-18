import collections
import re
from collections import *
from typing import List

class juniper:
    def __init__(self):
        pass

    def trans_addr(self, line, new_file_name) -> List:
        new_file = open(f'C:\\Users\\K1220006\\Desktop\\{new_file_name}.txt', 'w')
        fgt_addr = [i.split() for i in line if "set address" in i]
        new_file.write('config firewall address\n')

        for i in fgt_addr:
            # print('config firewall address', '\n','edit name {0}'.format(i[3]), '\n\t',
            #       'set subnet {0} {1}'.format(i[4], i[5]), '\n', 'next')
            #  #  프린트 하는 부분
            if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", i[4]):
                new_file.write(f'edit {i[3]}\nset subnet {i[4]} {i[5]}\nnext\n')
            else:
                new_file.write(f'edit {i[3]}\nset type fqdn\nset fqdn {i[4]}\nnext\n')
        new_file.write('\n')
        new_file.close()

        return new_file

    def trans_addrgrp(self, line, new_file_name) -> List:
        new_file = open(f'C:\\Users\\K1220006\\Desktop\\{new_file_name}.txt', 'w')
        new_file.write('config firewall address\n')

        temp_addrgrp = [i.split() for i in line if "set group address" in i]
        fgt_addrgrp = collections.defaultdict(list)
        for temp in temp_addrgrp:
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