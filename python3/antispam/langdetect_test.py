
#from wordfreq import word_frequency
#import wordfreq
import unicodedata as ud
import simplejson as json
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from langdetect import detect
#import plotly.plotly as plotly
#print(word_frequency('basketball','en'))
#print(wordfreq.zipf_frequency('北京地铁', 'zh'))
#fsample=open('/Users/jerrychi/Downloads/samplechat.csv','r')
#fspam=open('/Users/jerrychi/Downloads/Spam1.json','r')
#fham=open('/Users/jerrychi/Downloads/Ham1.json','r')
#file=open('/Users/jerrychi/Downloads/hamclean10000.csv','r')
fhamzh=open('/Users/jerrychi/Downloads/hamzh.csv','r')

count = 0

d_total = defaultdict(int)
d_correct = defaultdict(int)
for line in file:
    split = line.split(',')
    lang = split[0]
    msg = split[1]
    d_total[lang]+=1
    d_correct[]
    try:
        detected = detect(msg)[0:2]
    except:
        detected = 'error'
    if lang=='zh':
        print(lang + ' ' + detected)
    count += 1
    if count > 200:
        break

if False:
    for line in fham:
        linejson = json.loads(line, strict=False)
        lang = linejson['lang']
        msg = linejson['message']
        try:
            detected=detect(msg)
        except:
            detected='error'
        print(lang +' '+ detected)
        count+=1
        if count>300:
            break

