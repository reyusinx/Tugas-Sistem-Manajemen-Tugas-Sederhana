# Mengimpor semua fungsi dari modul Statistik, searchEngine, dan TugasManager
from Statistik import *
from searchEngine import *
from TugasManager import *

def main():
    # Loop utama program yang akan terus berjalan sampai user memilih keluar
    while True:
        # Menampilkan menu pilihan kepada user
        print("\n1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas")
        print("5. Cari Tugas")
        print("6. Statistik")
        print("7. Keluar")
        
        # Meminta input pilihan dari user
        choice = input("Pilih menu: ")
        
        # Handle pilihan menu 1: Menambah tugas baru
        if choice == '1':
            judul = input("Judul tugas: ") 
            deskripsi = input("Deskripsi tugas: ")  
            tambahTugas(judul, deskripsi)
            print("Tugas berhasil ditambahkan!")
            
        # Handle pilihan menu 2: Menampilkan semua tugas
        elif choice == '2':
            tampilkanTugas()
            
        # Handle pilihan menu 3: Menandai tugas sebagai selesai
        elif choice == '3':
            id_tugas = int(input("ID tugas yang selesai: "))  
            if tandaiTugas(id_tugas):
                print("Tugas ditandai selesai!")
            else:
                print("ID tugas tidak ditemukan.")
                
        # Handle pilihan menu 4: Menghapus tugas
        elif choice == '4':
            id_tugas = int(input("ID tugas yang dihapus: "))  
            if hapusTugas(id_tugas):
                print("Tugas dihapus!")
            else:
                print("ID tugas tidak ditemukan.")
                
        # Handle pilihan menu 5: Mencari tugas berdasarkan kata kunci
        elif choice == '5':
            keyword = input("Kata kunci pencarian: ")
            hasil = cariTugas(keyword)  
            if hasil:
                print("Hasil pencarian:")
                # Menampilkan setiap tugas yang ditemukan dengan statusnya
                for tugas in hasil: 
                    status = "✓" if tugas['selesai'] else "✗"  
                    print(f"{tugas['id']}. [{status}] {tugas['judul']} - {tugas['deskripsi']}")  
            else:
                print("Tugas tidak ditemukan.")
                
        # Handle pilihan menu 6: Menampilkan statistik tugas
        elif choice == '6':
            statistik()
            
        # Handle pilihan menu 7: Keluar dari program
        elif choice == '7':
            print("Sampai jumpa!")
            break  # Keluar dari loop while
            
        # Handle pilihan yang tidak valid
        else:
            print("Pilihan tidak valid.")

# Menampilkan header program yang menarik
print("\n" + "="*50)
print("Sistem Manajemen Tugas".center(50))
print("="*50)

# Menjalankan program utama
main()
