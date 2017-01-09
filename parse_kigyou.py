#in_file = open('/Users/jerrychi/Downloads/kigyou.txt', 'r')
out_file = open('/Users/jerrychi/Downloads/kigyou_out.csv',encoding='utf-8', mode='w')

import codecs
f = codecs.open('/Users/jerrychi/Downloads/kigyou.txt', encoding='utf-8')


#for line in f:
#    print repr(line)

count=0
comma_count=0
for line in f.readlines():
    if '（2' not in line and '輸出者等' not in line and '所在地' not in line and 'URL　' not in line :
        if line[0]=='〒':
            out_file.write("\n")
            comma_count=0
        if 'http' in line:
            line=line.replace('http','"'+','+'"'+'http')
        if line[0:3]=='www':
            line = line.replace('www', '"' + ',' + '"' + 'www')
        while ('http' in line or line[0:3]=='www') and comma_count<4:
            line=','+line
            comma_count+=1
      #  print('first is: ' + line)
       # print('"'+line[0:1000].rstrip() + '",')
        out_file.write('"'+line[0:1000].rstrip() + '",')  # if you want
        comma_count+=1

    count+=1
  #  if count>30:
   #     break

#=OFFSET(B2,-1,COUNTA(B1:I1)-1)

print 'a','\n','b'