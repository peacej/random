#in_file = open('/Users/jerrychi/Downloads/kigyou.txt', 'r')
out_file = open('/Users/jerrychi/Downloads/kigyou_out.csv',encoding='utf-8', mode='w+')

import codecs
f = codecs.open('/Users/jerrychi/Downloads/kigyou.txt', encoding='utf-8')


#for line in f:
#    print repr(line)

count=0
for line in f.readlines():
    out_file.write(line[0:10] + ',')  # if you want
    count += 1
    if count > 10:
        break
