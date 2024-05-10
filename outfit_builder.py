import numpy
import sklearn
import tensorflow
import pandas as pd

original_data = pd.read_csv('C:/Users/laura/Desktop/AI/styles.csv', on_bad_lines='skip')
original_data = original_data.drop_duplicates()
original_ = original_data.dropna()

import pandas as pd
import random

# Function to randomly select an item based on user input
def select_item(subcategory, gender, season, usage):
    items = original_data[(original_data['subCategory'] == subcategory) &
                          (original_data['gender'] == gender) &
                          (original_data['season'] == season) &
                          (original_data['usage'] == usage)]
    return items.sample(1)

# Specify characteristics
gender = input("Enter gender (Men/Women): ")
season = input("Enter season (Summer/Fall/Winter/Spring): ")
usage = input("Enter usage (Casual/Formal/Party): ")

# Randomly select one item from each subcategory
selected_items = {}
chance = random.randint(0,1)
if gender == 'Women' and chance==0:
    subcategories = ['Topwear', 'Bottomwear', 'Shoes', 'Bags', 'Jewellery']
elif gender == 'Women' and chance==1:
    subcategories = ['Dress', 'Shoes', 'Bags', 'Jewellery']
elif gender == 'Men':
    subcategories = ['Topwear', 'Bottomwear', 'Shoes', 'Watches']
for subcategory in subcategories:
    selected_items[subcategory] = select_item(subcategory, gender, season, usage)

# Display the selected items
print("\nSelected items:")
for subcategory, item in selected_items.items():
    print(f"{subcategory}: {item['productDisplayName'].values[0]}")