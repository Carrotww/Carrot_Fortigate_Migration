import sys
import math
import time

# file_lo = input('파일의 경로를 입력하세요 : ')
# file_name = input('파일의 이름을 입력하세요 : ')

# file_rlo = file_lo + file_name

# file = open('{0}{1}'.format(file_lo, file_name), mode='r')
forti_addr = []
forti_grp = []
forti_policy = []
forti_route = []
line = None

start_time = time.time()
file = open('C:\\Users\\K1220006\\Desktop\\미디어윌 ASA 5505.txt', mode='r')
file_data = file.read().splitlines()

forti_addr = [x for x in file_data if 'network-object' in x]
end_time = time.time()

print(forti_addr)
print(f"{end_time - start_time: .5f} sec")

# while line != '':
#     line = file.readline()
#     if 'network-object' in line:
#         print(line)
#     elif 'object-group network' in line:
#         pass
#