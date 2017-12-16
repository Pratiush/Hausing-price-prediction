import re
import pandas as pd
from datetime import datetime
import numpy as np

def file_open(str):
    f = open(str,'r')
    return f
stri = ["Bob.txt","Bright_Brothers.txt","Masters_of_Stones.txt","Not_Known.txt","The_Greens.txt","The_Kings.txt","The_Lannisters.txt","The_Ollivers.txt","The_Overlords.txt","The_Starks.txt","Wood_Priests.txt"]

#f= open('mob.txt','r')
#text = f.read()

# list of featuures to be extracted from text file.

l=['House ID','Dock','Capital','Royal Market','Guarding Tower','River','dining','bedrooms','Knight','bathrooms','blessed','Location','space','visit','renovation','curse','farm','Holy tree','Date']
d = {}


for i in range (0,11):
    f=file_open(stri[i])
    text = f.read()
    blocks= re.split('\n\n+',text)
    for i in  range (0,len(blocks)):
        lines =re.split('\n',blocks[i])
        for line in lines:
            if l[0] in line:
               hid = re.split(':',line)[1]
               hid=hid.lstrip()
               d[hid]={}
            if l[1] in line:
                d[hid]['Dock']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[2] in line :
                d[hid]['Capital']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[3] in line:
                d[hid]['Royal Market']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[4] in line:
                d[hid]['Guarding_tower']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[5] in line:
                d[hid]['River']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[8] in line:
                d[hid]['Knight']=float(re.search(r"[-+]?\d*\.\d+|\d+",line).group())
            if l[6] in line:
                d[hid]['dining']=int(re.search(r"\d+",line).group())
            if l[7] in line:
                d[hid]['bedrooms']= int(re.search(r"\d+",line).group())
            if l[9] in line:
                d[hid]['bathrooms'] = int(re.search(r"\d+",line).group())
            if l[10] in line:
                d[hid]['bless'] = int(re.search(r"\d+",line).group())
            if l[11] in line:
                d[hid]['Location'] = re.split(":",line)[1]
            if l[12] in line :
                if "no" in line:
                    d[hid]['space'] = 0
                else:
                    d[hid]['space'] =1
            if l[13] in line :
                if "couldn't" in line:
                    d[hid]['visit'] = 0
                else:
                    d[hid]['visit'] =1
            if l[14] in line :
                if "not" in line:
                    d[hid]['renovation'] = 0
                else:
                    d[hid]['renovation'] =1
            if l[15] in line :
                if "couldn't" in line:
                    d[hid]['curse'] = 0
                else:
                    d[hid]['curse'] =1
            if l[16] in line :
                if "small" in line:
                    d[hid]['farm'] = 0
                else:
                    d[hid]['farm'] =1
            if l[17] in line :
                if "tall" in line:
                    d[hid]['holy_tree'] = 1
                else:
                    d[hid]['holy_tree'] =0
            if l[18] in line:
                day = re.split("and",line)
                day1 = re.split(":",day[0])
                day2 = re.split(":",day[1])
                date1 = day1[1].lstrip()+":"+day1[2].lstrip()
                date2 = day2[1].lstrip()+":"+day2[2].lstrip()
                d[hid]['built'] = date1
                d[hid]['priced'] = date2
                

# DataFrame from dictionary
df = pd.DataFrame.from_dict(d,orient='index')

#DataFrame from csv
p = pd.DataFrame.from_csv("house_prices.csv")

# mapping price from the two DataFrame
p = p[np.isfinite(p['Golden Grains'])]
df['price'] =p['Golden Grains']
# complete dataset need to separate training and testing dataset
df.to_csv("final.csv")

