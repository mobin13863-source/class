class Book():
    def __init__(self, name, page):
        self.name = name
        self.page = page
    def open(self):
        answer = f'open the last page ({self.page})'
        return answer


class Darsi(Book):
    def __init__(self, name, page, Base, field):
        Book.__init__(self, name, page)
        self.Base = Base
        self.field = field


d = Darsi("programmer", "400_page", 3, "Computer")

print(d.open())