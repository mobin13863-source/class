class persone():

    ''' this object the first is give name and age after that can write anything
        second method give two number and return zarb thiose
        thired method give two number and return average thiose number
        '''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("obgect created")
        
        
    def zar(self, x, i= 1):# in this method i can to calculate zarb
        self.x =  x
        self.i = i
        res = x* i
        print("object zarb is created")
        return  res
        
        
    def avr(self, num1, num2):# in this function a can to calculate average
        self.num1 = num1
        self.num2 = num2
        avrrage = (num1 / num2)
        print("avr obgect is created")
        return avrrage
        
        
        
        
   
full = persone("MOBIN", 25)

print(f' my name is {full.name} and i {full.age} years old')
print()
