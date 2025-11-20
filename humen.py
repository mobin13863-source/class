class humen():
    '''
        in this a class I write abut Height, name, Favorite_food, tame_sleep, whah want to learn, 
        when he/she born, and now What year are we in now?
    
    '''

    def __init__(self, gad, name, fov_food, time_sleep, lern, birthday, in_year):
        
        self.gad = gad
        self.name = name
        self.fov_food = fov_food
        self.time_sleep = time_sleep
        self.lern = lern
        self.birthday = birthday
        self.in_year = in_year
        self.age = in_year - birthday
        
        
        
    def gad_function(self):
        return f' my gad is {self.gad} and and i have to make my time sleep , becose my time sleep is {self.time_sleep}'
    
    
    
    def lern_function(self):
        print( f' my name is {self.name} and my for food is {self.fov_food}')
        return f' i like to learn a bout {self.lern}'
    
    
    
    def age_humen(self):
        print( f' if i born in {self.birthday} and now in the {self.in_year} ')
        return f' so i shuld have be {self.age} age'
    


    def all_think(self):
        print( f' ok all things in my life is this, my name is {self.name} , i was born in {self.birthday} and i {self.age} years old')
        return f' i like to learn a {self.lern}, my fov_food is {self.fov_food}, my time_sleep is {self.time_sleep}'
    
    
    
persone = humen(190, "mobin","pasta", "10 pm", " programing", 2007, 2025)


print(persone.all_think())
    