#new type= Person which is an object
#name attribute
#talk method

class Person: #Person is object
    def __init__(self, name):
        self.name = name #Name is an attribute
    def talk(self): #talk is a method/function in Person object class
        print(f'Hi, i am {self.name}, How you doing?!')


caller1 = Person("John Smith") #caller1 is a variable

caller1.talk() #calling out talk function using variable
caller2 = Person("Suriyah Gokul")
caller2.talk()
