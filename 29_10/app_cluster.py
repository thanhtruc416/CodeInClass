# -*- coding: utf-8 -*-
from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Đọc dữ liệu đã lưu
df2 = pd.read_csv("customer_clusters.csv")

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
        clusters[c] = df2[df2['cluster']==c].to_dict(orient='records')
    return render_template_string(TEMPLATE, clusters=clusters)

if __name__ == '__main__':
    app.run(debug=True)
