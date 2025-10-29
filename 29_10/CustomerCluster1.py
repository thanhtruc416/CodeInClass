# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
import traceback
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px
from flask import Flask, render_template_string


# ============================
# KẾT NỐI MYSQL
# ============================
def getConnect(server, port, database, username, password):
    try:
        conn = pymysql.connect(
            host=server,
            port=port,
            user=username,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Kết nối MySQL thành công!")
        return conn
    except Exception as e:
        print("Lỗi kết nối MySQL:")
        traceback.print_exc()
        print(e)
        return None


def closeConnection(conn):
    if conn:
        conn.close()
        print("Đã đóng kết nối MySQL.")


def queryDataset(conn, sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = cursor.fetchall()
            df = pd.DataFrame(data)
            return df
    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu:")
        traceback.print_exc()
        print(e)
        return pd.DataFrame()


# ============================
# TRUY VẤN DỮ LIỆU
# ============================
conn = getConnect('localhost', 3306, 'salesdatabase', 'root', '@Obama123')
if conn:
    sql1 = "SELECT * FROM customer"
    df = queryDataset(conn, sql1)
    print(df)

sql2 = """
        SELECT DISTINCT c.CustomerID, c.Age, cs.Annual_Income, cs.Spending_Score
        FROM customer c
        JOIN customer_spend_score cs ON c.CustomerID = cs.CustomerID
    """
df2 = queryDataset(conn, sql2)
df2.columns = ['CustomerID', 'Age', 'Annual_Income', 'Spending_Score']
print(df2)
print("\n--- Dữ liệu customer_spend_score ---")
print(df2.head())

print("\n--- Thống kê mô tả ---")
print(df2.describe())


# ============================
# HÀM VẼ HISTOGRAM
# ============================
def showHistogram(df, columns):
    plt.figure(1, figsize=(7, 8))
    n = 0
    for column in columns:
        n += 1
        plt.subplot(3, 1, n)
        plt.subplots_adjust(hspace=0.5, wspace=0.5)
        sns.distplot(df[column], bins=32)
        plt.title(f"Histogram of {column}")
    plt.show()


showHistogram(df2, df2.columns[1:])


# ============================
# ELBOW METHOD
# ============================
def elbowMethod(df, columnsForElbow):
    X = df.loc[:, columnsForElbow].values
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n,
                       init="k-means++",
                       max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)
    plt.figure(1, figsize=(15, 6))
    plt.plot(range(1, 11), inertia, 'o')
    plt.plot(range(1, 11), inertia, '-', alpha=0.5)
    plt.xlabel("Number of clusters"), plt.ylabel("Cluster sum of squared distance")
    plt.show()


columns = ["Age", "Spending_Score"]
elbowMethod(df2, columns)


# ============================
# KMEANS
# ============================
def runKMeans(X, cluster):
    model = KMeans(n_clusters=cluster,
                   init='k-means++',
                   max_iter=500,
                   random_state=42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.fit_predict(X)
    return y_kmeans, centroids, labels


X = df2.loc[:, columns].values
cluster = 4
colors = ['red', 'green', 'blue', 'purple', 'black', 'pink', 'orange']
y_means, centroids, labels = runKMeans(X, cluster)
print(y_means)
print(centroids)
print(labels)
df2['cluster'] = labels


# ============================
# BIỂU ĐỒ KMEANS
# ============================
def visualizeKMeans(X, y_kmeans, cluster, title, xlabel, ylabel, colors):
    plt.figure(figsize=(10, 10))
    for i in range(cluster):
        plt.scatter(X[y_kmeans == i, 0],
                    X[y_kmeans == i, 1],
                    s=100,
                    c=colors[i],
                    label='Cluster %i' % (i + 1))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()


visualizeKMeans(X, y_means, cluster,
                "Clusters of Customer - Age X Spending Score",
                "Age", "Spending Score", colors)

print("-" * 20)
print("k=5")

columns = ['Annual_Income', 'Spending_Score']
elbowMethod(df2, columns)
X = df2.loc[:, columns].values
cluster = 5
y_means, centroids, labels = runKMeans(X, cluster)
print(y_means)
print(centroids)
print(labels)
df2['cluster'] = labels

visualizeKMeans(X, y_means, cluster,
                "Clusters of Customer - Annual Income X Spending Score",
                "Annual Income", "Spending Score", colors)

print("-" * 20)
print("k=6")

columns = ['Age', 'Annual_Income', 'Spending_Score']
elbowMethod(df2, columns)
X = df2.loc[:, columns].values
cluster = 6
y_means, centroids, labels = runKMeans(X, cluster)
print(y_means)
print(centroids)
print(labels)
df2['cluster'] = labels
print(df2)


# ============================
# BIỂU ĐỒ 3D
# ============================
def visualize3DKMeans(df, columns, hover_data, cluster):
    fig = px.scatter_3d(df,
                        x=columns[0],
                        y=columns[1],
                        z=columns[2],
                        color='cluster',
                        hover_data=hover_data,
                        category_orders={"cluster": range(0, cluster)})
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.show()


hover_data = df2.columns
visualize3DKMeans(df2, columns, hover_data, cluster)


# ============================
# HIỂN THỊ KẾT QUẢ TRÊN CONSOLE
# ============================
def showClusterDetailsConsole(df, cluster_col='cluster'):
    clusters = sorted(df[cluster_col].unique())
    print("\n===== DANH SÁCH KHÁCH HÀNG THEO CỤM =====")
    for c in clusters:
        print(f"\n CỤM {c} ({len(df[df[cluster_col] == c])} khách hàng)")
        print(df[df[cluster_col] == c][['CustomerID', 'Age', 'Annual_Income', 'Spending_Score']].to_string(index=False))


showClusterDetailsConsole(df2)
df2.to_csv("customer_clusters.csv", index=False)
print("💾 Đã lưu file customer_clusters.csv thành công!")


# ============================
# FLASK WEB HIỂN THỊ KẾT QUẢ
# ============================
app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Customer Clusters</title>
    <style>
        body {font-family: Arial; margin: 20px;}
        h1 {color: #2c3e50;}
        h2 {color: #34495e;}
        table {border-collapse: collapse; width: 100%; margin-bottom: 40px;}
        th, td {border: 1px solid #ccc; padding: 8px; text-align: center;}
        th {background-color: #3498db; color: white;}
        tr:nth-child(even) {background-color: #f9f9f9;}
    </style>
</head>
<body>
    <h1>Danh sách khách hàng theo từng cụm (Cluster)</h1>
    {% for c, data in clusters.items() %}
        <h2>Cụm {{ c }} ({{ data|length }} khách hàng)</h2>
        <table>
            <tr>
                {% for col in data[0].keys() %}
                    <th>{{ col }}</th>
                {% endfor %}
            </tr>
            {% for row in data %}
                <tr>
                    {% for col in row.values() %}
                        <td>{{ col }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </table>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def show_clusters():
    clusters = {}
    for c in sorted(df2['cluster'].unique()):
        clusters[c] = df2[df2['cluster'] == c].to_dict(orient='records')
    return render_template_string(TEMPLATE, clusters=clusters)



if __name__ == '__main__':
    import webbrowser
    import threading
    import os

    url = "http://127.0.0.1:5000"
    print(f"\n🌐 Flask server sẽ chạy tại: {url}")

    # Khi debug=True, Werkzeug chạy một process "reloader" rồi spawn process con.
    # Ta chỉ muốn mở browser 1 lần (ở process gốc), nên kiểm tra WERKZEUG_RUN_MAIN.
    def _open_browser():
        try:
            webbrowser.open_new(url)
        except Exception:
            pass

    # Nếu đang chạy lần đầu (chưa phải process chính của reloader), schedule mở browser.
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        threading.Timer(1.0, _open_browser).start()

    app.run(debug=True)
