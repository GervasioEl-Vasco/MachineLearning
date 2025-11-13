# Sistem Fuzzy Kontrol Suhu dan Kelembaban Kandang Ayam Berdasarkan Ras

## Deskripsi Projek

Program ini merupakan sistem kontrol logika fuzzy untuk mengatur kecepatan kipas kandang ayam berdasarkan tiga variabel utama:

- Suhu kandang (°C)

- Kelembaban udara (%)

- Ras ayam (pedaging, petelur, atau lokal)

Tujuan utamanya adalah menjaga kondisi mikroklimat kandang agar tetap nyaman dan optimal sesuai kebutuhan fisiologis masing-masing ras ayam, berdasarkan data nyata dari jurnal peternakan Indonesia seperti Ternak Tropika (2023), Jurnal Ilmu Ternak Unpad (2024), dan Chickin.id.

## Fitur Utama

- Input variabel fuzzy: suhu, kelembaban, dan ras ayam

- Output fuzzy: kecepatan kipas (%)

- Rule base yang berbeda untuk setiap jenis ras ayam

- Simulasi otomatis & interaktif

- Visualisasi fungsi keanggotaan (menggunakan matplotlib)

- Analisis perbandingan antar ras ayam terhadap suhu kandang

## Variabel dan Fungsi Keanggotaan
1. Input: Suhu Kandang (C)

| Kategori  | Range     | Keterangan                         |
| --------- | --------- | ---------------------------------- |
| dingin    | 15 – 25   | Suhu di bawah ideal                |
| normal    | 20 – 30   | Suhu optimal untuk pertumbuhan     |
| panas     | 25 – 40   |	Suhu tinggi yang perlu pendinginan |

2. Input: Kelembaban (%)
   
| Kategori  | Range     | Keterangan                                 |
| --------- | --------- | ----------------------------------------- |
| kering    | 40 – 70   | Udara terlalu kering                      |
| normal    | 60 – 90   | Suhu optimal untuk pertumbuhan            |
| lembab    | 80 – 100  |	Kelembaban tinggi, perlu ventilasi ekstra     |

3. Input: Ras Ayam

| Ras |	Nilai | Karakteristik |
| --------- | --------- | ----------------------------------------- |
| Pedaging (Broiler) | 1 | Sangat sensitif panas |
| Petelur (Layer) |	2	| Toleransi sedang |
| Lokal (Kampung) |	3	| Tahan panas dan kelembaban tinggi |

4. Output: Kecepatan Kipas (%)

| Kategori | Range | Keterangan |
| --------- | --------- | ----------------------------------------- |
| lambat | 0 – 40 |	Kondisi sejuk |
|sedang |	20 – 80 |	Kondisi normal |
|cepat	| 60 – 100 | Kandang panas, perlu pendinginan |

## Rule Base (Contoh)

| Suhu | Kelembaban |	Ras Ayam | Output |
| --------- | --------- | -------- | -------- | 
| panas |	normal | pedaging | cepat |
| nyaman | lembab |	petelur |	sedang |
| dingin | kering |	lokal |	lambat |

Total ada 27 aturan (rules) untuk mengakomodasi kombinasi suhu, kelembaban, dan ras ayam.

## Struktur Kode
1. Definisi variabel fuzzy (suhu, kelembaban, ras_ayam, kipas)
2. Pembuatan fungsi keanggotaan dengan trimf()
3. Penentuan rule base (aturan fuzzy)
4. Pembuatan sistem kontrol (ControlSystem)
5. Fungsi konversi nama ras → nilai numerik
6. Pengujian dengan berbagai ras & kondisi suhu
7. Visualisasi fungsi keanggotaan
8. Simulasi interaktif melalui input terminal
9. Analisis pengaruh ras terhadap kecepatan kipas

## Cara Menjalankan Program
1. Instal dependensi

- Pastikan Python sudah terpasang, lalu install pustaka yang diperlukan:
```command
pip install numpy scikit-fuzzy matplotlib
```

2. Jalankan program
```command
python fuzzy_kandang_ayam.py
```

3️. Simulasi interaktif

Program akan meminta input:

Masukkan suhu kandang (°C) [15-40]:

Masukkan kelembaban (%) [40-100]:

Pilih ras ayam:

1. Pedaging/Broiler
2. Petelur/Layer
3. Lokal/Kampung

Output akan menampilkan:

- Kecepatan kipas (%)

- Status kondisi kandang

- Rekomendasi sistem

## Contoh Hasil Output

Ras: PEDAGING (Broiler)

Suhu: 35°C, Kelembaban: 75%

Kecepatan Kipas: 91.40%

Rekomendasi: KIPAS CEPAT - Butuh pendinginan ekstra!

## Referensi Datasheet

- Chickin.id. “Berapa Suhu dan Kelembaban Ideal Kandang Ayam?”

- Jurnal Ilmu Ternak Unpad (2024). Pengaruh Kepadatan Kandang Ayam Broiler Close-House Terhadap Mikroklimat.

- Jurnal Ternak Tropika (2023). Microclimate Analysis of Broiler Rearing.

- Edufarmers.org. Modul Budi Daya Ayam Layer.
  
----------------------------------------------------------------------------

***program ini masih dalam pengembangan***
