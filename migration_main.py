import sys

# file_lo = input('파일의 경로를 입력하세요 : ')
# file_name = input('파일의 이름을 입력하세요 : ')

# file_rlo = file_lo + file_name

# file = open('{0}{1}'.format(file_lo, file_name), mode='r')
forti_addr = []
forti_grp = []
forti_policy = []
forti_route = []
line = None
file = open('C:\\Users\\유형석\\Desktop\\hey.txt', mode='r')

# file_read = file.readline()
while line != '':
    line = file.readline()
    if 'network-object' in line:
        print(line, end='')
        # forti_addr.append()
    elif 'object-group network' in line:
        pass
        # forti_grp.append()

file.close()

print(type(line))