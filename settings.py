import json 

class Setting():
    def __init__(self,file,text):
        self.file=file
        self.text=text
    def read_config(self):
        with open(self.file, "r") as jsonFile:
            data = json.load(jsonFile)
        return data
    def save_config(self,data):
        with open(self.file, "w") as jsonFile:
            json.dump(data, jsonFile)
    def read_user(self):
        data=self.read_config()
        a=0
        for item in data:
            print(item)
            data[item]=self.text[a]
            a=a+1
        self.save_config(data)
     
      