from agents import Bot
from locations import Home, Market, Job, Fun

MINIMUM_BALANCE = 15
def go_to(location_cls, agent):
    if agent.location != location_cls.__name__:
        location_cls(agent)
        
def updateBotState(agent: Bot):
    # If hungry and has food, go home and eat
    if agent.hunger > 0.7 and agent.food:
        if agent.location != 'Home':
            go_to(Home,agent)
        Home(agent).eat(agent)

    # If hungry but no food, go to market to buy food
    elif agent.hunger > 0.7 and not agent.food:
        if agent.location != 'Market':
            go_to(Market,agent)
        food_items = Market(agent).buy(agent)
        if not food_items:
            if agent.location != 'Job':
                go_to(Job,agent)
            Job(agent).work(agent)

    # If tired, go home and sleep
    elif agent.energy < 0.4:
        if agent.location != 'Home':
            go_to(Home,agent)
        Home(agent).sleep(agent)

    # If low on money or food, work
    elif agent.money < MINIMUM_BALANCE or not agent.food:
        if agent.location != 'Job':
            go_to(Job,agent)
        Job(agent).work(agent)

    # If unhappy and rich enough, party
    elif agent.mood < 0.5 and agent.money >= 20:
        if agent.location != 'Fun Place':
            go_to(Fun,agent)
        Fun(agent).party(agent)

    # Nothing urgent
    else:
        agent.current_action = 'Idle'
        return 'idle'