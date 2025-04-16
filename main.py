'''
Aplikasi Feed Berita
'''
import berita_terbaru_tribun

if __name__ == "__main__":
    print("Aplikasi Utama")
    result = berita_terbaru_tribun.ekstraksi_data()
    berita_terbaru_tribun.tampilkan_data(result)