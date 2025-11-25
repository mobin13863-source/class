# i use polymophezami in class

class runnig():
    def __init__(self, name):
        self.name = name
    def action(self):
        return f'{self.name} is runnig'
    
class riding():
    def __init__(self, name):
        self.name = name
    def action(self):
        return f'{self.name} is biking'
    
mobin = runnig("mobin")
asma = riding("asma")  


for persone in [mobin, asma]:
    print(persone.action())
    '''
    Description
       ok mybe namas is Different byt the (action) is some  and work one think
       so in the this code Mobin and Asma are the same variable called persone
       after that I print persone with method action and we sould not forget
       define instance with like name (mobin) and (asma)

    '''
     
