#!pip install tensorflow
#!pip install scikit-learn

import numpy
import sklearn
import tensorflow
import pandas as pd

# Load the dataset
data = pd.read_csv('C:/Users/laura/Desktop/AI/styles.csv', on_bad_lines='skip')
data.head()

# Clean the data (remove duplicates, handle missing values, etc.)
data = data.drop_duplicates()
data = data.dropna()

# Transform categorical variables into numerical representations
data['gender'] = pd.Categorical(data['gender']).codes
data['masterCategory'] = pd.Categorical(data['masterCategory']).codes
data['subCategory'] = pd.Categorical(data['subCategory']).codes
data['articleType'] = pd.Categorical(data['articleType']).codes
data['baseColour'] = pd.Categorical(data['baseColour']).codes
data['season'] = pd.Categorical(data['season']).codes
data['usage'] = pd.Categorical(data['usage']).codes

data

from sklearn.metrics.pairwise import cosine_similarity
# Assuming we have a user-item matrix with clothing features
item_features = data[["gender", "masterCategory", "subCategory", "articleType", "baseColour", "season", "year", "usage"]]

# Calculate cosine similarity between item features
similarity_matrix = cosine_similarity(item_features)
similarity_matrix

similarity_matrix.shape

# Create a similarity score feature for each item
item_similarity_scores = similarity_matrix.mean(axis=1)

def recommend_similar_items(item_name, top_n=5):
    # Check if item_name is in the dataset
    if item_name not in data['productDisplayName'].values:
        print(f"Item '{item_name}' not found in the dataset.")
        return
    
    # Find the index of the item in the dataset
    item_index = data[data['productDisplayName'] == item_name].index[0]
    
    # Get the similarity scores for the given item
    item_similarities = similarity_matrix[item_index]
    
    # Get indices of top similar items
    similar_indices = item_similarities.argsort()[::-1][1:top_n+1]  # Exclude itself
    
    # Get the names of top similar items
    similar_items = data.iloc[similar_indices]['productDisplayName'].values
    
    return similar_items

# Example usage:
user_input_item = input("Which item do you want similar recommendations for?")
recommended_items = recommend_similar_items(user_input_item)
print(f"Recommended items similar to '{user_input_item}':")
for item in recommended_items:
    print(item)