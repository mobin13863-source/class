class circle():
    '''
    just return Area in second method 
    '''
    
    
    pi = 3.1415926
    def __init__(self, r):
        self.r = r
        
    def masaht(self):
        m = self.r * self.r * circle.pi
        return m
    
    
    
c1 = circle(10)

print(c1.masaht())
        