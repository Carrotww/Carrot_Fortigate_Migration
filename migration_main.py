import re
import sys
import juniper

# file_lo = input('파일의 경로를 입력하세요 : ')
# file_name = input('파일의 이름을 입력하세요 : ')

# file_rlo = file_lo + file_name
# https://velog.io/@learningssik/Github-%EC%8B%A0%EC%83%81-%EB%B1%83%EC%A7%80-5%EB%B6%84%EB%A7%8C%EC%97%90-%EC%96%BB%EB%8A%94-%EB%B0%A9%EB%B2%95
# file = open('{0}{1}'.format(file_lo, file_name), mode='r')
forti_addr = []
forti_grp = []
forti_policy = []
forti_route = []
line = None

if __name__ == '__main__':
    # file_path = input("Enter the file path : ") # File path input line
    # file = open('C:\\Users\\hsyu5\\Desktop\\KG passone.txt', 'r')
    # file = open('C:\\Users\\K1220004\\Desktop\\KG passone.txt', 'r') # company desktop file path
    file = open('C:\\Users\\K1220006\\Desktop\\위비스 config.txt', 'r') # home desktop file path

    line = file.readlines() # line = file을 읽어와 한 줄 씩 부여줌
    jun = juniper.juniper() # import juniper class juniper
    fgt_addr_filename = input("Enter the New addr_filename : ")
    fgt_addrgrp_filename = input("Enter the New addrgrp_filename : ")

    fgt_addr = jun.trans_addr(line, fgt_addr_filename)
    fgt_addrgrp = jun.trans_addrgrp(line, fgt_addrgrp_filename)
    # print(fgt_addrgrp)
    # print(fgt_addr)

    file.close()

# file_data = file.read().splitlines()
# forti_addr = [x for x in file_data if 'network-object' in x]
# forti_addr = [x.lstrip() for x in forti_addr]
# for i in forti_addr:  # is not in subnet each element, + /32 or is there subnet, then store another list
#     pass
# print('config firewall Address', '\n', 'edit name {0}', '\n\t', 'set subnet {1}', 'u\n',
#       'next')

# for line in test:
#     s_result = []
#     i = 0
#     while i < len(line):
#         temp_str = line[i]
#         if line[i][0] == '"' and line[i][-1] != '"':
#             i += 1
#             while line[i][-1] != '"':
#                 temp_str += line[i]
#                 i += 1
#             temp_str += line[i]
#         i += 1
#         s_result.append(temp_str)
#     result.append(s_result)