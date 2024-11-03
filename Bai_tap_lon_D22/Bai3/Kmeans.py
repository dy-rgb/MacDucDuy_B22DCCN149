import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

file_path = 'results.csv'
data = pd.read_csv(file_path)

numeric_data = data.select_dtypes(include=['float64', 'int64'])
numeric_data = numeric_data.fillna(numeric_data.mean()).dropna()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(scaled_data)
print("Phân nhóm các cầu thủ dựa trên các chỉ số:")
for i in range(num_clusters):
    print(f"\nNhóm {i+1}:")
    cluster_data = data[data['Cluster'] == i]
    print(cluster_data[['Name'] + list(numeric_data.columns)])