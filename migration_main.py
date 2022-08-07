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
    # file = open('C:\\Users\\hsyu5\\Desktop\\KG passone.txt', 'r')
    # file_path = input("Enter the file path : ") # File path input line
    file = open('C:\\Users\\K1220004\\Desktop\\KG passone.txt', 'r') # company desktop file path
    # file = open(file_path, 'r')
    line = file.readlines()
    jun = juniper.juniper()
    new_file = open('C:\\Users\\K1220004\\Desktop\\test.txt', 'w')
    a = jun.trans_addr(line, new_file)
    print(a)
    file.close()

# file_data = file.read().splitlines()
# forti_addr = [x for x in file_data if 'network-object' in x]
# forti_addr = [x.lstrip() for x in forti_addr]
# for i in forti_addr:  # is not in subnet each element, + /32 or is there subnet, then store another list
#     pass
# print('config firewall Address', '\n', 'edit name {0}', '\n\t', 'set subnet {1}', 'u\n',
#       'next')

# while line != '':
#     line = file.readline()
#     line2 = line.rstrip('\n')
#     if 'network-object' in line2:
#         forti_addr.append(line2)
#         print(line2)
#     elif 'object-group network' in line:
#         pass