import pandas as pd
import numpy as np
import random

df= pd.read_excel("D:\Data Analyst\Pricing_dataset.xlsx")
print(df.head())

# Encode the Categorical Variables

demand_map={'low':0,'medium':1,'high':2}
inventory_map={'low':0,'medium':1,'high':2}

df['demand_level'] = df['demand_level'].map(demand_map)
df['inventory_level'] =df['inventory_level'].map(inventory_map)

# State creation
def get_state(row):
    return (
        row['demand_level'],
        row['inventory_level'],
        int(row['competitor_price']/50)
   )

states=[get_state(row) for _,row in df.iterrows()]
unique_states = list(set(states))

state_to_index = {state:id for id, state in enumerate(unique_states)}

# Actions
actions ={0:-50,1:0,2:50}

num_states = len(unique_states)
num_actions = len(actions)

print(num_states)
print(num_actions)

# Apply Q-Theory

Q = np.zeros((num_states,num_actions))

# Setting up the parameters
alpha = 0.1
gamma =0.6
epsilon = 0.2
episodes =500

# Demand Simulation
def simulate_sales(price, competitor_price, demand_level):
    base = demand_level*10 +25  # Initial value of base

    if price < competitor_price:
       base +=6
    elif price > competitor_price: 
       base -=6  
    noise = random.randint(-3,3)   

    return max(base + noise,0)  

#Reward Function

def calculate_reward(price,sales):
    revenue = price *sales
    return revenue

# Training

for episode in range(episodes):
     for i in range(len(df) -1):
        row= df.iloc[i]   # Current row -> present market
        next_row= df.iloc[i+1]  # next row -> Future market

        state = state_to_index[get_state(row)]
        next_state = state_to_index[get_state(next_row)]

        if random.uniform(0,1) < epsilon:   # Perform Exploration
            action = random.choice(list(actions.keys()))
        else:
            action =np.argmax(Q[state])     # Perform Explotiation

        price_change =actions[action]    

        new_price = row['current_price']+price_change

        sales = simulate_sales(new_price,row['competitor_price'],row['demand_level'])

        reward = calculate_reward(new_price,sales)

        old_value = Q[state,action]
        next_max =np.max(Q[next_state])

        # new_value calculation
        new_value = old_value +alpha*(reward+gamma* next_max -old_value)

        Q[state,action] = new_value

     # Finalizing the policy
     
print("\n Learned Pricing Policy")
for state,id, in state_to_index.items():
         best_action = np.argmax(Q[id]) 
         decision = actions[best_action]

         if decision == -50:
             label ="Reduce Price"
         elif decision ==0:
             label =="Keep the same Price"   
         else:
             label ="Increase Price" 

print(f"State {state} -->{label}")     
                
        