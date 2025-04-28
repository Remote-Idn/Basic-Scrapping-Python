'''
Aplikasi Feed Berita CNN Indonesia
'''
import berita_terbaru_cnn

if __name__ == "__main__":
    print("Berita CNN Indonesia")
    result = berita_terbaru_cnn.ekstraksi_data()
    berita_terbaru_cnn.tampilkan_data(result)