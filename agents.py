import uuid
class Bot:
    def __init__(self,name:str):
        self.name  = name
        self.id  = uuid.uuid4()

        self.location = 'Home'
        self.current_action = 'idle'
        self.last_tick = 0
        
        self.food = []
        self.money = 0
        self.sleep = 0
        self.energy = 1.0
        self.hunger = 0
        self.mood = 0.5
        self.social = 0.5
        self.memory=[]

    def __repr__(self):
        return(f'Name:{self.name}, Id:{self.id}')