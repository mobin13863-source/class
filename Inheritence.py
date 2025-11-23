class Book():
    def __init__(self, name, page):
        self.name = name
        self.page = page


class Darsi(Book):
    def __init__(self, name, page, Base, field):
        Book.__init__(self, name, page)
        self.Base = Base
        self.field = field


d = Darsi("programmer", "400_page", 3, "Computer")

print(d.name)