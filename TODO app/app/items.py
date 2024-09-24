
from datetime import date

class Item(object):
    """docstring for Items."""

    def __init__(self,text="",title="",date=date.today()):
        super(Item, self).__init__()
        self.id=0
        self.title=title
        self.text=text
        self.done=False
        self.date=date

    def setDone(self,done):
       self.done=done

    def getDone(self):
        if self.done==True or self.done=="option2":
           return "completato"
        elif self.done==False or self.done=="option1":
            return "incompleto"

    def setTitle(self,input):
        self.text=input

    def setText(self,input):
        self.title=input

    def getText(self):
        return self.text

    def getTitle(self):
        return self.title

    def getDate(self):
        dateString=str(self.date)
        return dateString
    
    def setId(self,idNuovo):
        self.id=idNuovo

    def getId(self):
        return self.id

    
    
    