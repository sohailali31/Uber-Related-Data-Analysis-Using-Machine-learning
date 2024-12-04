from flask import Flask, render_template, request
import folium
from folium.plugins import MarkerCluster
from sklearn.cluster import KMeans
import pandas as pd

app = Flask(__name__)

# Load data and fit KMeans once at startup
data = pd.read_csv(r"C:\Users\moham\OneDrive\Desktop\uber-raw-data-sep14.csv")
X = data[['Lat', 'Lon']]
kmeans = KMeans(n_clusters=7, random_state=42).fit(X)
centroids = kmeans.cluster_centers_

def generate_map(lat, lon, predicted_cluster):
    """Generates a folium map centered on the input coordinates and adds cluster markers."""
    map_object = folium.Map(location=[float(lat), float(lon)], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(map_object)

    # Add cluster centroid markers
    for index, point in enumerate(centroids):
        color = 'blue' if index == predicted_cluster else 'green'
        folium.Marker(
            location=point,
            popup=f'Cluster {index}: {point}',
            icon=folium.DivIcon(html=f'''
                <div style="font-size: 12pt; font-weight: bold; color: white; background-color: {color}; border-radius: 50%; width: 25px; height: 25px; display: flex; justify-content: center; align-items: center;">
                    {index + 1}
                </div>''')
        ).add_to(marker_cluster)

    # Add marker for the selected point
    folium.Marker(
        location=[float(lat), float(lon)],
        popup='Predicted point',
        icon=folium.Icon(icon='star', color='red')
    ).add_to(map_object)

    return map_object._repr_html_()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        
        # Predict cluster based on input lat/lon
        cluster = kmeans.predict([[float(lat), float(lon)]])[0]
        
        # Generate map with markers
        map_html = generate_map(lat, lon, cluster)
        
        return render_template('index.html', lat=lat, lon=lon, cluster=cluster, map=map_html)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
