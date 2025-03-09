# Uber-Related Data Analysis Using Machine Learning

This project uses Flask, Folium, and K-Means clustering to analyze Uber-related data, visualize clusters on a map, and predict cluster locations based on user input coordinates.

## Features
- Load Uber dataset and apply K-Means clustering.
- Visualize cluster centroids on an interactive Folium map.
- Predict cluster membership based on user-provided latitude and longitude.
- Display an interactive map with markers for clusters and user input locations.

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/sohailali31/Uber-Related-Data-Analysis-Using-Machine-learning.git
cd Uber-Related-Data-Analysis-Using-Machine-learning
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage
1. Open the web app in a browser.
2. Enter latitude and longitude values.
3. Click submit to see the predicted cluster and an interactive map with cluster centroids.

## Technologies Used
- **Python**
- **Flask** (for web framework)
- **Folium** (for interactive maps)
- **Scikit-learn** (for K-Means clustering)
- **Pandas** (for data manipulation)

## Dataset
The dataset used is `uber-raw-data-sep14.csv`, which contains latitude and longitude points of Uber pickups in September 2014.
Link to the dataset: https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city

## License
This project is open-source and available under the [MIT License](LICENSE).



