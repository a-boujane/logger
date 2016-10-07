import pprint
import json
import requests
class Logger:
    def __init__(self):
        self.dico={};
        self.locations = {};
    
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
            self.locateOne(key)
        return self.locations


    def locateOne(self, ipAddress):
        url = "http://www.freegeoip.net/json/"
        url=url+ipAddress
        resp = requests.get(url)
        if resp.status_code ==200:
            jo = resp.json()
            temp ={}
            temp["latitude"]= jo["latitude"]
            temp["longitude"]= jo["longitude"]
            self.locations[ipAddress]=temp
            return self.locations