import pandas as pd
import numpy as np

data = pd.read_csv('results.csv')

def find_top_bottom_players(data):
    top_players = {}
    bottom_players = {}
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        top_players[column] = data.nlargest(3, column)[['Name', column]]
        bottom_players[column] = data.nsmallest(3, column)[['Name', column]]
    return top_players, bottom_players

top_players, bottom_players = find_top_bottom_players(data)
print("Top 3 cầu thủ có giá trị cao nhất ở mỗi chỉ số:")
for attr, top in top_players.items():
    print(f"\nChỉ số: {attr}")
    print(top)
print("-----------------------------------------------")
print("\nTop 3 cầu thủ có giá trị thấp nhất ở mỗi chỉ số:")
for attr, bottom in bottom_players.items():
    print(f"\nChỉ số: {attr}")
    print(bottom)
