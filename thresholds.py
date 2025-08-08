from agents import Bot
from locations import Home, Market, Job
def updateBotState(agent:Bot):
    if agent.hunger > 0.7:
        if len(agent.food) == 0:
            pass
        if not agent.location == 'Home':
            pass
        else:
            Home(Bot).eat(Bot)
    
