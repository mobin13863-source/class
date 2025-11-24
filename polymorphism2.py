# i use polymophezami in class
#and i call the names with anither function

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

def show(persine):
    return persine.action()

print(show(mobin))
print(show(asma))

