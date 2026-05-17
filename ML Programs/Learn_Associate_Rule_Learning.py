import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

transaction_data = [

   ['Milk','Bread'],
   ['Milk','Butter'],
   ['Bread','Butter'],
   ['Milk','Bread','Butter'],
   ['Milk','Bread','Eggs'],
   ['Soft Drinks','Chips'],
   ['Hot Drinks','Chips'],
   ['Chips','Peanuts','Samosa'],
   ['Chats','Samosa'],
   ['Milk','Bread','Butter','Eggs']
]

# Convert to one hot encoded format

all_items = sorted (list(set(item for data in transaction_data for item in data)))

print(all_items)

# Create Basket Matrix

basket_values =[]

for data in transaction_data:
    row ={}
    for item in all_items:
        row[item]=item in data

    basket_values.append(row)

basket_Matrix = pd.DataFrame(basket_values)    

print(basket_Matrix.head())

# Apply Apriori Algorithm
frequent_itemsets =apriori(basket_Matrix,min_support =0.3,use_colnames=True)

print(frequent_itemsets)

# Defining the association rules

rules = association_rules(frequent_itemsets,metric='confidence',min_threshold=0.5)

print("\n Association Rules:")

print(rules[['antecedents','consequents','support','confidence','lift']])

# sort based on Lift

sorted_rules= rules.sort_values(by ='lift',ascending =False)

print("\n Top Rules sorted by Lift")

print(sorted_rules[['antecedents','consequents','support','confidence','lift']].head())

# Business Insights

for index, row in sorted_rules.iterrows():
    antecedents = list(row['antecedents'])
    consequents = list(row['consequents'])
    support =row['support']
    confidence =row['confidence']
    lift =row['lift']

    print(f"If Customer buys {antecedents}")
    print(f"Then customer also buys {consequents}")

    print(f"Support:{support:.2f}")
    print(f"confidence:{confidence:.2f}")
    print(f"lift:{lift:.2f}")

    if lift >1:
        print("Positive Product Association")