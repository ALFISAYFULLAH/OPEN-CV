Deskripsi Proyek
Proyek ini merupakan aplikasi pengolahan citra menggunakan OpenCV dan Python. Terdapat berbagai skrip untuk memproses citra dan hasil output seperti citra yang diubah ukurannya, diblur, diberi tepi, dan diberi ambang batas.
File yang Terdapat

main.py: Skrip utama untuk pengolahan citra.
camera-test.py: Skrip untuk pengujian terkait kamera.
output.mp4: File output video.
cropped.jpg, gray.jpg, hsv.jpg, main.jpg, resized.jpg, resume.png, hari_3_blur.jpg, edges.jpg, image.jpg, main.png, threshold.jpg, pic.jpg: File citra yang telah diproses.
.gitignore: File untuk mengecualikan file tertentu dari kontrol versi.
venv/: Direktori lingkungan virtual.

Penyiapan

Pastikan Python dan OpenCV sudah terinstal.
Klon repository dan masuk ke direktori proyek.
Aktifkan lingkungan virtual: source venv/bin/activate (Linux/Mac) atau venv\Scripts\activate (Windows).
Instal dependensi jika ada (contoh: pip install opencv-python).

Cara Penggunaan
Jalankan main.py untuk memproses citra. Modifikasi skrip sesuai kebutuhan untuk menyesuaikan parameter pengolahan citra.
Penjelasan dengan Gambar
Berikut adalah tampilan lingkungan proyek di editor kode (contoh: Visual Studio Code) yang menunjukkan struktur file dan output terminal:


Kiri: Panel eksplorasi menunjukkan file seperti main.py, citra yang diproses, dan file konfigurasi.
Kanan Atas: File readme.md yang sedang diedit.
Kanan Bawah: Terminal menunjukkan error terkait fungsi resize di main.py (baris 5), yang perlu diperbaiki.

Catatan

Proyek ini mengalami error asersi terkait fungsi resize. Periksa fungsi tersebut di main.py (baris 5) untuk debugging.
Pastikan semua file citra tersedia di direktori proyek.
