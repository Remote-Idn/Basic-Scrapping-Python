def ekstraksi_data():
    hasil = dict()
    hasil["judul"] = "Rekonstruksi Kasus 3 Polisi Meninggal Ditembak Kopda Basar Digelar Besok"
    hasil["waktu"] = "26 menit lalu"
    return hasil


def tampilkan_data(result):
    print("Berita Terbaru Tribun Lampung")
    print(f"Judul Berita: {result["judul"]}")
    print(f"Waktu terbit: {result["waktu"]}")