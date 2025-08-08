from agents import Bot
class Home:
    def __init__(self,agent:Bot):
        self.location = 'Home'
        agent.location = self.location
        agent.current_action = 'Idle'

    @staticmethod
    def sleep(agent:Bot):
        agent.energy+=0.1
        agent.mood+=-0.05
        agent.current_action = 'Sleeping'
    
    @staticmethod
    def eat(agent:Bot):
        agent.current_action = 'Eating'
        food = {'info':{'saturation_value':0}}
        food_index = 0
        for i,_ in enumerate(agent.food):
            if agent.food[i]['info']['saturation_value'] > food['info']['saturation_value']:
                food = agent.food[i]
                food_index = i
        agent.hunger -= food['info']['saturation_value']
        agent.energy += food['info']['energy_value']
        agent.food[food_index]['quantity']-=1
        if agent.food[food_index]['quantity'] == 0:
            agent.food.pop(i)

class Market:
    def __init__(self,agent:Bot):
        self.location = 'Market'
        agent.location = self.location

    @staticmethod
    def view_menu():
        Items = [{'name':'Bread','price':5,'info':{'energy_value':0.3,'saturation_value':0.3}},
                {'name':'Meat','price':8,'info':{'energy_value':0.5,'saturation_value':0.5}}]
        return Items
    
    def analyze_goods(self,agent:Bot):
        Items = self.view_menu()
        options = []
        for item_dict in Items:
            quantity = agent.money//item_dict['price']
            if quantity == 0:
                continue
            
            tspq = (item_dict['info']['saturation_value'])/item_dict['price']
            options.append({'name':item_dict['name'],'quantity':quantity,'tspq':tspq})
        
        if not options:
            return False
        viable_option = max(options, key=lambda x: x['tspq'])
        return viable_option

    def buy(self,agent:Bot):
        agent.current_action = 'Buying'

        Items = self.view_menu()
        viable_option = self.analyze_goods(agent)

        if not viable_option:
            return False

        item = viable_option['name']
        quantity = viable_option['quantity']

        
        food_order = None

        for item_dict in Items:
            if item == item_dict['name']:
                food_order = item_dict
                break

        if not food_order:
            return False
        
        agent.money-=food_order['price']*quantity

        #if item exists in inventory
        for owned_food in agent.food:
            if owned_food['name'] == food_order['name']:
                owned_food['quantity'] += quantity
                return f'Bought {quantity} {item}'
            
        #if item doesnt exist in inventory    
        agent.food.append({'name':food_order['name'],'quantity':quantity,'info':food_order['info']})
        return f'Added {quantity}  {food_order["name"]} '

class Job:
    def __init__(self,agent:Bot):
        self.location = 'Job'
        agent.location = self.location

    @staticmethod
    def work(agent:Bot):
        agent.current_action = 'At Work'
        agent.money+=5
        agent.energy-=0.1
        agent.mood+=0.05
        
class Fun:
    def __init__(self,agent:Bot):
        self.location = 'Fun Place'
        agent.location = self.location
        agent.current_action = 'Enjoying life.'
    
    @staticmethod
    def party(agent:Bot):
        agent.money-=10
        agent.energy-=0.2
        agent.mood+=0.2