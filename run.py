import re
import math
import cmath 
f1=open("file1.txt", "r")
f2=open("file2.txt", "r")
lines1= f1.readlines()
lines2= f2.readlines()
d1={}
d2={}
for i in lines1:
    for x in filter(None, re.split("[\n., \-!?:]+",i)):
        if d1.get(x):
            d1[x]=d1[x]+1
        else:
            d1[x]=1

for i in lines2:
    for x in filter(None, re.split("[\n., \-!?:]+",i)):
        if d2.get(x):
            d2[x]=d2[x]+1
        else:
            d2[x]=1

sumT=0
for i in d1.keys():
    if d2.get(i):
        sumT+=d1[i]*d2[i]
sum1=0
for i in d1.keys():
    sum1+=d1[i]*d1[i]
sum2=0
for i in d2.keys():
    sum2+=d2[i]*d2[i]
m=(math.sqrt(sum1)*math.sqrt(sum2))
angle=cmath.acos(sumT/m)
print(angle)
