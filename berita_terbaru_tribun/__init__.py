import requests
from bs4 import BeautifulSoup

def ekstraksi_data():

    try:
        content = requests.get('https://www.cnnindonesia.com/tag/kebijakan-tarif-donald-trump')
    except Exception:
        return None

    if content.status_code == 200:
        print(content.status_code)
    else:
        return
        print(content.status_code)

    soup = BeautifulSoup(content.text, "html.parser")
    content_tag = soup.find('div', {'class': "flex flex-col gap-5"})
    if content.status_code == 200:
        judul = soup.find('h2', {'class': "text-cnn_black_light dark:text-white mb-2 inline leading-normal text-xl group-hover:text-cnn_red"})
        link = soup.find('a', {'href': "flex group items-center gap-4"})
        waktu = soup.find('span', {'class': "text-xs text-cnn_black_light3"})
    else:
        print('Berita tidak ditemukan')


    hasil = dict()
    #hasil['berita'] = berita
    hasil["judul"] = judul.text
    hasil["link"] = link
    hasil["waktu"] = waktu.text
    return hasil

def tampilkan_data(result):
    if result is None:
        return 'pass'
    print('Berita Terbaru CNN Indonesia')
    print(f'{result["judul"]}')
    print(f'{result["link"]}')
    print(f'{result["waktu"]}')



