import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_pie_chart(df):
    # Hitung jumlah data berdasarkan kategori
    data_major_category = df['Major_category'].value_counts()

    # Warna latar belakang dan warna teks yang ingin Anda gunakan
    background_color = '#A6D1E6'  # Warna secondary
    text_color = '#3D3C42'  # Warna quaternary

    # Buat pie chart untuk Major Category
    plt.figure(figsize=(8, 6), facecolor=background_color)  # Atur warna latar belakang di sini
    plt.pie(data_major_category, labels=data_major_category.index, autopct='%1.1f%%', startangle=140, textprops={'color': text_color})
    plt.axis('equal')

    # Simpan pie chart ke dalam bentuk bytes
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar sebagai string base64
    img_base64 = base64.b64encode(img.getvalue()).decode()

    # Tutup plot
    plt.close()

    return img_base64

def generate_bar_chart(df):
    # Hitung jumlah data berdasarkan kategori
    data_employed = df.groupby('Major_category')['Employed'].sum()

    # Warna latar belakang dan warna teks yang ingin Anda gunakan
    background_color = '#D8D3CD'  # Warna secondary
    text_color = '#797A7E'  # Warna quaternary

    # Buat diagram batang untuk kolom Employed
    plt.figure(figsize=(10, 6), facecolor=background_color)  # Atur warna latar belakang di sini
    data_employed.plot(kind='bar', color='#E0ECE4')  # Warna primary untuk bar chart
    plt.ylabel('Employed', color=text_color)  # Atur warna teks
    plt.xticks(rotation=45, color=text_color)  # Rotasi label sumbu x untuk kejelasan dan atur warna teks

    # Simpan diagram batang ke dalam bentuk bytes
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar sebagai string base64
    img_base64 = base64.b64encode(img.getvalue()).decode()

    # Tutup plot
    plt.close()

    return img_base64
