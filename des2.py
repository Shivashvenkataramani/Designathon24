import requests
import time
time.sleep(5)
s = " https://api.thingspeak.com/update?api_key=Q4H9ZZGNMV5CXJ5E&field1="
with open ("resultsdes.txt","r") as f:
    L = f.readlines()
ss = list(L)
print(L)
for i in ss:
    if i == "[" or i == "]" or i == '"' or i == "'" or i==",":
        i = i+1
    else:
       u = str(s)
       print(u+i)
       requests.get(s+i)
       list(s)