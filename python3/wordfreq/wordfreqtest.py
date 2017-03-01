### Pyspark data extraction:
# hamclean = spark.read.parquet('s3://supercell-antichatbot-prod/data/ham_clean')
#hamsub = hamclean.limit(10000).coalesce(1)
#hamsub.write.csv('s3://supercell-antichatbot-prod/data/ham_clean_csv/hamclean10000')
#hamclean.filter("lang='zh'").select('lang','message','source').coalesce(1).write.csv('s3://supercell-antichatbot-prod/data/ham_clean_csv/hamzh')

#from wordfreq import word_frequency
import wordfreq
import unicodedata as ud
import simplejson as json
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

#import plotly.plotly as plotly
#print(word_frequency('basketball','en'))
print(wordfreq.zipf_frequency('北', 'zh'))
fsample=open('/Users/jerrychi/Downloads/samplechat.csv','r')
fspam=open('/Users/jerrychi/Downloads/Spam1.json','r')
fham=open('/Users/jerrychi/Downloads/Ham1.json','r')
fham10k=open('/Users/jerrychi/Downloads/hamclean10000.csv','r')
plt.style.use('seaborn-deep')
results=[] #list of lists
results_hhi=[]
maxlines=0

fham10k=open('/Users/jerrychi/Downloads/hamclean10000.csv','r')
chinese_rows=0
tempcount=0
for line in fham10k:
    split = line.split(',')
    if len(split)<2:
        continue
    lang = split[0]
    msg = split[1]
    #tempcount+=1
    #if tempcount>20:
    #    break
    if lang=='zh':
        chinese_rows+=1

print(chinese_rows)

def avg_word_freq(file,format='json'):
    global maxlines
    count = 0
    catcount_list = []
    hhi_list = []
    for line in file:
        if maxlines!=0 and count>maxlines:
        #if count>15:
            break
        if(format=='json'):
            msg = json.loads(line,strict=False)['message']
        else:
            msg = line.split(',')[0]
        charfreq_list=[]
        for char in msg:
            charfreq_list.append()
        #print(msg,wordfreq.zipf_frequency(msg, 'zh'))
        #print(msg,catcount,len(catcount))
        catcount_list.append(len(catcount))
        #HHI = herfindhal index https://en.wikipedia.org/wiki/Herfindahl_index
        hhi = sum([(freq / len(msg)) ** 2 for freq in catcount.values()])
        hhi_list.append(hhi)
        count+=1
    if maxlines==0:
        maxlines=count
    print('average is ',sum(catcount_list)/len(catcount_list))
    results.append(catcount_list)
    results_hhi.append(hhi_list)
    #
    #y, binEdges = np.histogram(catcount_list, bins=10)
    #bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
    #plt.plot(bincenters, y, '-')

print('\n','################ BELOW IS HAM ############','\n')
unicode_cat_count(fham)
print('\n','################ BELOW IS SPAM ############','\n')
unicode_cat_count(fspam)
print('\n','################ BELOW IS RANDOM SAMPLE ############','\n')
unicode_cat_count(fsample,format='csv')
#plt.hist(results,np.linspace(0,15,15),label=['ham','spam','rand sample'])
plt.hist(results_hhi,np.linspace(0,1,20),label=['ham','spam','rand sample'])
plt.legend(loc='best')
plt.ylabel('frequency (count of messages)')
#plt.xlabel('# of unicode categories')
plt.xlabel('Herfindahl index of frequency of each unicode category in each message')
plt.show()




