import pandas as pd
import matplotlib.pyplot as plt
import math

file_path = 'results.csv'
data = pd.read_csv(file_path)
metric_columns = data.select_dtypes(include=['float64', 'int64']).columns
teams = data['Team'].unique()
def plot_team_histograms(team_name, team_data, metrics, plots_per_page=20):
    num_metrics = len(metrics)
    num_pages = math.ceil(num_metrics / plots_per_page)

    for page in range(num_pages):
        plt.figure(figsize=(15, 10))
        for i in range(plots_per_page):
            metric_idx = page * plots_per_page + i
            if metric_idx >= num_metrics:
                break
            metric = metrics[metric_idx]
            plt.subplot(5, 4, i + 1)  
            plt.hist(team_data[metric].dropna(), bins=15, color='red', edgecolor='black')
            plt.title(f'{metric}', fontsize=10)
        plt.suptitle(f'{team_name} - Page {page + 1}', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()
for team in teams:
    team_data = data[data['Team'] == team]
    plot_team_histograms(team, team_data, metric_columns)
