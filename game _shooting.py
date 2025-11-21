class player():
    
    Magazine = 10
    Enemy = 10
    bag_player = ('water', 'bread', 'knife') 
    
    def __init__(self, shot, run, koole):
        self.shot = shot
        self.run = run
        self.koole = koole

        print("playing game is start ")
        res = input('do you wnat to play (Y/N)')
        if res.upper() not in ["Y" , "YAS", "ARE"]:
            print("nice to meet you")
            exit()
        

    def shoting(self):
        print(f'ok you have {player.Magazine} magazines')
        try:
            res = int(input('have many do you want to use (1/10)? '))
        except ValueError:
            print('plase enter number')
            return
        
        if 1 <= res <= 10:
            ramaining = player.Magazine - res
            print(f'ok, you used {res} magazines')
            print(f'Now you have {ramaining} left')
            print(f'Enemies is come {player.Enemy}')
            
        else:
             print('choes number betwen 1 and 10')
        answer = input('now do you want run or wath your bag')
        if answer == 'bag':
            self.bag()
        else:
             self.runing()

             
    def runing(self):
            print('ok you want to run ')
            print("Game over ")
            
            
    def bag(self):
            print('you decide to wath in the bag (bag/run)?  ')
            print(f"when you start You had [{player.bag_player}]")
            print(f"Now you have {player.bag_player[-1]}")
            
            ansewr_to_fight = input("Where do you want to hit them, you (heart/head)? ").lower()
            if ansewr_to_fight == 'head':
                print("you can't Enemy is pro")
                print("good game you die") 
            elif ansewr_to_fight == "heart":
                print("well You succeeded")
                



game = player('knife', 'walk', 'bag')
print(player.shoting)

            
                
            
                
            
                