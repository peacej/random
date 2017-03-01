
#from wordfreq import word_frequency
#import wordfreq
import unicodedata as ud
import simplejson as json
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

#import plotly.plotly as plotly
#print(word_frequency('basketball','en'))
#print(wordfreq.zipf_frequency('北京地铁', 'zh'))
fsample=open('/Users/jerrychi/Downloads/samplechat.csv','r')
fspam=open('/Users/jerrychi/Downloads/Spam1.json','r')
#fham=open('/Users/jerrychi/Downloads/Ham1.json','r')
fhamzh=open('/Users/jerrychi/Downloads/hamzh.csv','r')

zhlist = []
spampath = '/Users/jerrychi/Downloads/spamgz/'
for filename in os.listdir(spampath):
    for line in gzip.GzipFile(spampath+filename):
        if line[]



plt.style.use('seaborn-deep')
results=[] #list of lists
results_hhi=[]
maxlines=0

def unicode_cat_count(file,format='json',print_under_thresh=False):
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
        catcount = defaultdict(int)
        for char in msg:
            catcount[ud.category(char)]+=1
        #print(msg,wordfreq.zipf_frequency(msg, 'zh'))
        #print(msg,catcount,len(catcount))
        catcount_list.append(len(catcount))
        #HHI = herfindhal index https://en.wikipedia.org/wiki/Herfindahl_index
        hhi = sum([(freq / len(msg)) ** 2 for freq in catcount.values()])
        if hhi<0.5 and print_under_thresh==True:
            print(msg)
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
unicode_cat_count(fhamzh,print_under_thresh=True,format='csv')
print('\n','################ BELOW IS SPAM ############','\n')
#unicode_cat_count(fspam)
print('\n','################ BELOW IS RANDOM SAMPLE ############','\n')
#unicode_cat_count(fsample,format='csv')
#plt.hist(results,np.linspace(0,15,15),label=['ham','spam','rand sample'])
#plt.hist(results_hhi,np.linspace(0,1,20),label=['ham','spam','rand sample'])
plt.hist(results_hhi,np.linspace(0,1,40),label=['chinese ham'])
plt.legend(loc='best')
plt.ylabel('frequency (count of messages)')
#plt.xlabel('# of unicode categories')
plt.xlabel('Herfindahl index of frequency of each unicode category in each message')
plt.show()




