class student():
    '''
    
    this class return a name and age that student and you can 
    use a infotmation function and see the name and age
    after that you can see the aveage of grades and
    you can call and use the function grades
    
    '''
    
    
    def __init__(self, name, age, grades):
        
        self.name = name
        self.age = age
        self.grades = grades
        print("information is done")
        
        
    def information(self):
        '''
        retunr a information student
        '''
        return f' name student is {self.name} and the age is {self.age}'
    
    
    def grades_s(self):
        '''
        this method return a avrage betwen student grades
        and if avreage more 16 print something else print 
        enather something
        
        '''
        res = sum(self.grades) / len(self.grades)
        if res > 16:
            print("well done you stady hard")
        else:
            print('you shoud more stady')
        return int(res)
    
    
    
    def best_grades(self):
        '''
           in this method return a best grades in the list
        
        '''
        best = self.grades[0]
        for i in self.grades:
            if best < i:
                best = i
                if best == 20:
                    print('you shoud go to best schol ')
        return f'your best grades is {best}'
                
            
        

al = student("mobin", 18, [10,20, 14, 2])

print(al.best_grades())
print()
print(al.grades_s())
