import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

file_path = 'results.csv'
data = pd.read_csv(file_path)

numeric_data = data.select_dtypes(include=['float64', 'int64']).copy()
numeric_data.fillna(numeric_data.mean(), inplace=True)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

sse = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(K, sse, marker='o')
plt.xlabel('Số cụm k')
plt.ylabel('Tổng bình phương sai số trong cụm (SSE)')
plt.title('Elbow Method for Optimal k')
plt.show()
