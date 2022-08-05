import re
from typing import List

class juniper:
    def __init__(self):
        pass

    def trans_addr(self, line, new_line) -> List:
        fgt_addr = [i.split() for i in line if "set address" in i]
        new_line.write('config firewall address\n')

        for i in fgt_addr:
            print('config firewall address', '\n','edit name {0}'.format(i[3]), '\n\t',
                  'set subnet {0} {1}'.format(i[4], i[5]), '\n', 'next')
            new_line.write('edit ')
            new_line.write(i[3])
            new_line.write('\n')
            new_line.write('set subnet ')
            new_line.write(i[4])
            new_line.write(' ')
            new_line.write(i[5])
            new_line.write('\n')
            new_line.write('next\n')
        new_line.write('\n')

    def trans_service(self, line) -> List:
        re_service = re.compile("service")
        data_service = re_service.search(line)
        return data_service

    def trans_manageip(self, line) -> List:
        re_manageip = re.compile("")