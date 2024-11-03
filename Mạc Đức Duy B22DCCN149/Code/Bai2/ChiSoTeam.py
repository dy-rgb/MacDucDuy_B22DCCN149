import pandas as pd

file_path = 'results.csv'
data = pd.read_csv(file_path)
print("Các cột trong bảng dữ liệu:", data.columns)
numeric_data = data.select_dtypes(include=['float64', 'int64'])
teams = data['Team'].unique()
results = {'Team': ['All']}
for col in numeric_data.columns:
    results[f'Median Of {col.capitalize()}'] = [numeric_data[col].median()]
    results[f'Mean Of {col.capitalize()}'] = [numeric_data[col].mean()]
    results[f'Std Of {col.capitalize()}'] = [numeric_data[col].std()]
for team in teams:
    team_data = numeric_data[data['Team'] == team]
    results['Team'].append(team)
    for col in numeric_data.columns:
        results[f'Median Of {col.capitalize()}'].append(team_data[col].median())
        results[f'Mean Of {col.capitalize()}'].append(team_data[col].mean())
        results[f'Std Of {col.capitalize()}'].append(team_data[col].std())

results_df = pd.DataFrame(results)
output_path = 'results2.csv'
results_df.to_csv(output_path, index=False)
#print(f"Kết quả đã được lưu vào file: {output_path}")