class classname:
    def __init__(self):
        self.classes = {}

    def addclass(self,name):
        if name in self.classes:
          print(name + 'already exist')
        if name not in self.classes:
           self.classes[name] = { } 

    def delectClass(self,name):
        if name in self.classes:
          del self.classes[name]
        if name not in self.classes:
           print(name + 'Does not exist!')

    def rename(self,name,newname):
       if name not in self.classes:
          print (name + "does not exist")
       if name in self.classes:
         self.classes[newname] = self.classes.pop(name)






    