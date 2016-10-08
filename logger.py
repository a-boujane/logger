import pprint
import json
import requests
import threading
import time
import Queue
class Logger:
    
    def __init__(self):
        self.dico={};
        self.locations = {};
        self.lock = threading.Lock()
        self.timing=[]
        self.sm= threading.BoundedSemaphore(value=40)
    def addItems(self,*keys):
        for key in keys:
            if(key in self.dico):
                self.dico[key]+=1
            else:
                self.dico[key]=1
    
    def stringify(self):
        for key in self.dico:
            self.dico[key]=str(self.dico[key])

    def getHighest(self):
        highest=0;
        for key in self.dico:
            if(highest<self.dico[key]):
                highest=self.dico[key]
        return highest;
    
    def prDico(self):
        pprint.pprint(self.dico);

    def toJson(self, path):
        file=open(path,'w+')
        json.dump(self.dico,file)
        file.close

    def locate(self):
        
        for key in self.dico:
            thread = threading.Thread(target=self.locateOne,args=(key,),name="3bdssssslaaaaam"+key).start()   
        while threading.activeCount()>1:
            time.sleep(0.1)
        return self.locations

    def locateOne(self, ipAddress):
        url = "http://www.freegeoip.net/json/"
        url=url+ipAddress
        self.sm.acquire()
        start = time.time()
        
        resp = requests.get(url)
        self.timing.append(time.time()-start)
        self.sm.release()
        if resp.status_code ==200:
            jo = resp.json()
            temp ={}
            temp["latitude"]= jo["latitude"]
            temp["longitude"]= jo["longitude"]
            self.lock.acquire()
            try:
                self.locations[ipAddress]=temp
            finally:
                self.lock.release()
