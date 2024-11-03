import pandas as pd

file_path = 'results.csv'
data = pd.read_csv(file_path)
numeric_data = data.select_dtypes(include=['float64', 'int64'])
top_teams = {}
for col in numeric_data.columns:
    max_score = data[col].max()
    top_team = data[data[col] == max_score]['Team'].values[0]  
    top_teams[col] = (top_team, max_score)

print("Đội bóng có điểm số cao nhất ở mỗi chỉ số:")
for stat, (team, score) in top_teams.items():
    print(f"{stat}: {team} với điểm số {score}")