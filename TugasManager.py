# Variabel global untuk menyimpan semua tugas dalam bentuk list
penyimpanan = []

def tambahTugas(judul, deskripsi):
    # Menambah tugas baru ke dalam daftar (By Value - membuat objek baru)
    tugasBaru = {
        'id': len(penyimpanan) + 1,  # ID otomatis berdasarkan jumlah tugas
        'judul': judul,
        'deskripsi': deskripsi,
        'selesai': False  # Status awal selalu belum selesai
    }
    penyimpanan.append(tugasBaru)  # Menambahkan tugas baru ke penyimpanan

def tampilkanTugas():
    # Menampilkan daftar tugas
    if not penyimpanan:  # Jika tidak ada tugas
        print("Tidak ada tugas.")
        return
    
    # Loop melalui setiap tugas dan tampilkan informasinya
    for tugas in penyimpanan:  
        # Tentukan status berdasarkan nilai 'selesai'
        if tugas['selesai']:
            status = "✓"  # Centang untuk tugas selesai
        else:
            status = "✗"  # X untuk tugas belum selesai
        
        # Tampilkan tugas dengan format yang rapi
        print(f"{tugas['id']}. [{status}] {tugas['judul']} - {tugas['deskripsi']}")

def tandaiTugas(id_tugas):
    # Menandai tugas sebagai selesai (By Reference - mengubah objek langsung)
    for tugas in penyimpanan:  
        if tugas['id'] == id_tugas:  # Cari tugas dengan ID yang sesuai
            tugas['selesai'] = True  # Ubah status menjadi selesai
            return True  # Berhasil menandai
    return False  # Gagal menemukan tugas dengan ID tersebut

def hapusTugas(id_tugas):
    # Menghapus tugas berdasarkan ID
    for i, tugas in enumerate(penyimpanan):  # Loop dengan index dan nilai
        if tugas['id'] == id_tugas:  # Cari tugas dengan ID yang sesuai
            del penyimpanan[i]  # Hapus tugas dari penyimpanan
            return True  # Berhasil menghapus
    return False  # Gagal menemukan tugas dengan ID tersebut
