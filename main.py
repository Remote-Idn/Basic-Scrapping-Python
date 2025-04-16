'''
Aplikasi Feed Berita
'''
from berita_terbaru_tribun import ekstraksi_data, tampilkan_data

if __name__ == "__main__":
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)