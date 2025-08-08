from agents import Bot
from thresholds import updateBotState
import time

class Main():
    def run_simulation(ticks=100):
        agent = Bot('feroz')
        with open('results.txt','a') as file:
         for tick in range(ticks):
            # print(f"\nTick {tick + 1}")
        
        # Simulate passive decay
            agent.hunger += 0.05  # gets hungrier
            agent.energy -= 0.03  # gets tired
            agent.hunger = min(agent.hunger, 1.0)
            agent.energy = max(agent.energy, 0.0)

        # Update bot's decision
            updateBotState(agent)
            file.write(f'\nTick:{tick+1},Location:{agent.location},Action:{agent.current_action},Money:{agent.money},Hunger: {agent.hunger:.2f},Energy: {agent.energy:.2f},Mood: {agent.mood:.2f},Food: {[(f['name'], f['quantity']) for f in agent.food]}')
        # Print status
            # print(f"Location: {agent.location}")
            # print(f"Action: {agent.current_action}")
            # print(f"Money: {agent.money:.2f}")
            # print(f"Hunger: {agent.hunger:.2f}")
            # print(f"Energy: {agent.energy:.2f}")
            # print(f"Mood: {agent.mood:.2f}")
            # print(f"Food: {[(f['name'], f['quantity']) for f in agent.food]}")
            
        # Delay (optional for realism)
            time.sleep(0.2)

            # print("\nSimulation ended.")


if __name__ == '__main__':
    Main.run_simulation()