# 📊 Analisis Pelanggan Bike Sharing dengan Streamlit 🚲

Proyek ini bertujuan untuk menganalisis jumlah pelanggan bike sharing berdasarkan musim serta membandingkan pengguna casual dan registered.

## 📌 Fitur
- Menampilkan total pelanggan berdasarkan musim dalam bentuk visualisasi.
- Perbandingan jumlah pengguna casual dan registered berdasarkan waktu.
- Tampilan interaktif dengan **Streamlit**.

---

## ⚙️ Setup Environment - Anaconda
```sh
conda create --name main-ds python=3.12.7
conda activate main-ds
pip install -r requirements.txt
```

## ⚙️ Setup Environment - Shell/Terminal
```sh
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Menjalankan Aplikasi
```sh
streamlit run dashoboard/dashboard.py
```

---

## 📂 Struktur Folder
```
📁 submission
├────dashboard
| ├── 📜 dashboard.py      # File utama Streamlit
| └── 📜 main_data.csv  
├────data
| ├── 📜 day.csv          # Dataset yang digunakan
| └── 📜 hour.csv         # Dataset yang digunakan
├── 📜 requirements.txt  # Dependensi yang diperlukan
├── 📜 README.md         # Dokumentasi proyek
└── 📜 url.txt         # url streamlit
```

