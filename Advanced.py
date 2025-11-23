# i use overrite in Inheritance
class Book():
    def __init__(self, name, page):
        self.name = name
        self.page = page
    def opne(self):
        return f'opnend {self.name}, with ({self.page})'


class Darsi(Book):
    def __init__(self,name, page, paye, reshti):
        Book.__init__(self, name, page)
        self.paye = paye
        self.reshti = reshti
    def open(self):
        return f' opennd {self.name}, in {self.reshti}, with {self.paye}'
    

d = Darsi("programmer", 300, 5, "tajrobe")

print(d.open())