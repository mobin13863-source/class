class Humen():
    def __init__(self, name):
        self.name = name
        pass
    def jump(self):
        raise NotImplementedError("jumo the implemented")

class programmer(Humen):
    pass
    def jump(self):
        return(f'{self.name}, is jumped')


mobin = programmer("mobin")
print(mobin.jump())

# or i can write this

def show(programmer):
    return mobin.jump()
print(show("mobin"))

