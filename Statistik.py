# Mengimpor variabel penyimpanan dari modul TugasManager untuk mengakses data tugas
from TugasManager import penyimpanan

def statistik():
    """Menampilkan statistik tugas"""
    # Menghitung total jumlah tugas
    total = len(penyimpanan)
    
    # Menghitung jumlah tugas yang sudah selesai
    selesai = 0
    for task in penyimpanan:
        if task['selesai']:  # Jika tugas sudah selesai
            selesai += 1
    
    # Menghitung jumlah tugas yang belum selesai
    pending = total - selesai
    
    # Menampilkan statistik kepada user
    print("\nStatistik Tugas:")
    print(f"Total: {total}")
    print(f"Selesai: {selesai}")
    print(f"Belum Selesai: {pending}")
