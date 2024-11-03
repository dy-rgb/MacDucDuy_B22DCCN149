import pandas as pd
import matplotlib.pyplot as plt


file_path = 'results.csv' 
data = pd.read_csv(file_path)

numeric_data = data.select_dtypes(include=['float64', 'int64'])
plots_per_page = 20 
num_pages = (len(numeric_data.columns) + plots_per_page - 1) // plots_per_page  

for page in range(num_pages):
    fig, axes = plt.subplots(4, 5, figsize=(15, 10)) 
    axes = axes.flatten()
    start_col = page * plots_per_page
    end_col = min(start_col + plots_per_page, len(numeric_data.columns))
    for i, col in enumerate(numeric_data.columns[start_col:end_col]):
        axes[i].hist(numeric_data[col].dropna(), bins=20, color='red', edgecolor='black')
        axes[i].set_title(col, fontsize=10)
        axes[i].set_xlabel('', fontsize=8)
        axes[i].set_ylabel('', fontsize=8)
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.suptitle(f'Biểu đồ phân bố (Trang {page + 1}/{num_pages})', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    plt.show()