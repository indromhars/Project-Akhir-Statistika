from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from chart import *
import pickle

app = Flask(__name__, template_folder="templates")
model = pickle.load(open("train/model.pkl", "rb"))
file_path = 'data/all-ages.csv'
df = pd.read_csv(file_path)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/chart')
def chart():
    # Generate pie chart
    pie_chart_data = generate_pie_chart(df)

    # Generate bar chart
    bar_chart_data = generate_bar_chart(df)

    # Render template HTML dengan gambar yang telah dibuat
    return render_template('pages/chart.html', pie_chart_data=pie_chart_data, bar_chart_data=bar_chart_data)

@app.route('/major', methods=['GET', 'POST'])
def major():
    if request.method == 'POST':
        # Ambil data dari kolom 'Major'
        majors = df['Major'].tolist()

        # Initialize list to store numeric features
        numeric_features = []

        # Loop through form keys and check if value is numeric
        for key, value in request.form.items():
            # Skip 'Major' key
            if key == 'Major':
                major_input = value  # Simpan nilai 'Major' untuk digunakan dalam pesan
                continue
            try:
                # Convert value to float and append to numeric_features list
                numeric_features.append(float(value))
            except ValueError:
                # If value cannot be converted to float, ignore it
                pass
        
        # Convert numeric features to numpy array
        features = np.array([numeric_features])

        # Predict unemployment rate
        prediction = model.predict(features)

        # Scale prediction to percentage
        scaled_prediction = prediction[0] * 100

        # Render template with prediction and majors
        return render_template('pages/major.html', prediction_text='{} unemployment percentage is {:.2f}%'.format(major_input, scaled_prediction), majors=majors)

    else:
        # Ambil data dari kolom 'Major'
        majors = df['Major'].tolist()

        return render_template('pages/major.html', majors=majors)

if __name__ == '__main__':
    app.run(debug=True)
