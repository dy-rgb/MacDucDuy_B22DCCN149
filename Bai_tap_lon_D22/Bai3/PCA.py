import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

file_path = 'results.csv'
data = pd.read_csv(file_path)
numeric_data = data.select_dtypes(include=['float64', 'int64'])
numeric_data = numeric_data.fillna(numeric_data.mean())
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
data['Cluster'] = kmeans.fit_predict(scaled_data)
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)
plt.figure(figsize=(10, 7))
for i in range(num_clusters):
    cluster_points = reduced_data[data['Cluster'] == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Nhóm {i+1}')
plt.title('Phân nhóm cầu thủ bằng K-means (sau khi PCA)')
plt.legend()
plt.show()