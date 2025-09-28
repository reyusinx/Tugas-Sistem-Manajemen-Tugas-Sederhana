# Mengimpor variabel penyimpanan dari modul TugasManager untuk mengakses data tugas
from TugasManager import penyimpanan

def cariTugas(keyword, index=0, results=None):
    # Fungsi rekursif untuk mencari tugas berdasarkan kata kunci
    # Inisialisasi list results jika belum ada
    if results is None:
        results = []
    
    # Base case: jika index sudah melebihi jumlah tugas, kembalikan hasil
    if index >= len(penyimpanan):
        return results
    
    # Ambil tugas pada posisi index saat ini
    Tugas = penyimpanan[index]
    
    # Cek apakah keyword ada dalam judul atau deskripsi tugas (case insensitive)
    if (keyword.lower() in Tugas['judul'].lower() or 
        keyword.lower() in Tugas['deskripsi'].lower()):
        results.append(Tugas)  # Tambahkan tugas ke hasil jika cocok
    
    # Recursive call: panggil fungsi sendiri dengan index berikutnya
    return cariTugas(keyword, index + 1, results)
