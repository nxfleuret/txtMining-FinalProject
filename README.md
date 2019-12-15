# txtMining-FinalProject
Text Classification using Naive Bayes

# Projek akhir Text Mining

Projek akhir text mining dengan judul Klasifikasi Jurnal Berdasarkan Abstrak Menggunakan Metode Naïve Bayes disusun oleh:

#### Kelompok 8
- Alfredo Juan Pratama  175150201111012
- Kevin Aryo Wicaksono  175150201111039
- Reinhard Jonathan Silalahi 175150200111040

## Tentang program

Program ini ditujukan untuk mengklasifikasi dokumen berdasarkan data latih yaitu 30 dokumen pada tugas sebelumnya.

Program ini berisikan folder dan file

- **dataTest** - Folder yang berisikan data yang diujikan pada laporan
- **input** - Folder yang berisikan data latih yang digunakan oleh program
- **output** - Folder yang berisikan data hasil perhitungan seperti Raw-TF dan hasil dari preprocessing
- **Classification.py** - Kode program untuk melakukan klasifikasi
- **Main.py** - Kode program untuk melakukan proses secara keseluruhan
- **PreProcessing.py** - Kode program untuk melakukan proses preprocessing dokumen
- **Weighting.py** - Kode program untuk melakukan weighting
- **remove.txt & stoplist.txt** - File teks yang digunakan dalam tahap filtering pada preprocessing.

## Cara menggunakan

Program ini dapat digunakan dengan menjalankan file Main.py dengan mengganti kode **dataTest/dataSet-6.txt** pada Main.py baris 27
python
dataTest = open("dataTest/dataSet-6.txt", errors = 'ignore').read()

dan hasil keluaran program bisa ditentukan file trace HasilKlasifikasi.txt pada folder output. hal ini bisa diatur dalam file main.py
python
filenew = open("output/trace hasilKlasifikasi.txt", "a")
