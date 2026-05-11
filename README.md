# blackbox-testing 
## Sistem Peminjaman Ruang Diskusi Kampus

### Identitas Mahasiswa
- Nama  : Irene Noer Ramadhany
- NIM   : 235150207111064

### Deskripsi
Repository ini berisi implementasi pengujian Black-Box Testing pada studi kasus Sistem Peminjaman Ruang Diskusi Kampus untuk memenuhi tugas mata kuliah Pengujian Perangkat Lunak.

### Requirement Sistem

**1) FR-01: Validasi Durasi Pinjam**
- Durasi peminjaman harus 1–4 jam
- Jika di luar rentang maka sistem menolak

**2) FR-02: Aturan Peminjaman Ruang**

Mahasiswa dapat meminjam ruang jika:
- Mahasiswa terdaftar
- Tidak memiliki pelanggaran
- Ruang tersedia
  
**3) FR-03: Status Ruang**
- Ruang hanya bisa dipinjam jika AVAILABLE
- Tidak boleh loncat state

### Pengujian yang Dilakukan
- Equivalence Partitioning (EP)
- Boundary Value Analysis (BVA)
- Decision Table Testing
- State Transition Testing

### Struktur File
1) testing_ruang.py → Source code pengujian Python
2) Q1-235150207111064.pdf → Laporan pengujian
3) screenshot-output.png → Bukti hasil eksekusi program
4) README.md → Dokumentasi repository

### Cara Menjalankan
Jalankan program dengan perintah:
python testing_ruang.py



