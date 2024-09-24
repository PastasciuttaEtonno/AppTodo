from app.items import Item

class ListItem(Item):
    """docstring for List."""

    def __init__(self):
        super(ListItem, self).__init__()
        self.lista=[]
        self.count=0

    def getList(self):
        return self.lista

    def addItem(self,obj):
        self.lista.append(obj)

    def getLastItem(self):
        return self.lista[-1]

    def getSelectedItem(self,id):
        for i in range(len(self.lista)):
            if self.lista[i].getId()==id:
                return self.lista[i]

    def changeId(self):
        self.lista[-1].setId(self.count)
        self.count+=1

    def deleteItem(self,obj):
        self.lista.remove(obj)
