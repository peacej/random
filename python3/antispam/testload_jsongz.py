import gzip
import os
import json
count=0
path = '/Users/jerrychi/Downloads/spamgz/'
filecount=0
for filename in os.listdir(path):
    linecount=0
    for line in gzip.GzipFile(path+filename):
        print(json.loads(line,strict=False)['message'])
        linecount+=1
        if linecount>300:
            break
    filecount+=1
    if filecount >0:
        break

#print(count)