#to create new list like print.functions

class Suri:
    def __init__(self, x, y): #Constructors
        self.x = x
        self.y = y

    def adit(self):
        print('a+b')
    def sbit(self):
        print('a-b')
    def mbit(self):
        print('a*b')

output1 = Suri(10,20)
print(output1.y)


output = Suri()
print(output.adit())
print(output.sbit())
print(output.mbit())

#Suri() is an object
#Adding attributes to classes:

Suri1 = Suri()
Suri1.a = 10
Suri1.b = 20
print(Suri1.a)
Suri2 = Suri()
Suri2.aa = 100
Suri2.ab = 200
print(Suri2.ab)



