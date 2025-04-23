import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    #a = 1
    #for page in range(0):
    url = f'https://www.cnnindonesia.com'
    ge = requests.get(url).text
    soup = BeautifulSoup(ge, 'html.parser')
    li = soup.find('div', {'class': "overflow-y-auto relative h-[322px]"})
    lin = li.findAll('article')
    for y in lin:
            judul = y.find('h2', {'class': "text-base text-cnn_black_light group-hover:text-cnn_red"})
            link = y.find('a'), {'href'}
            #waktu = y.find('span', {'class': "text-xs text-cnn_black_light3"})
    else:
        print('Tidak ada data')

        y = dict()
        y["judul"] = judul.text
        y["link"] = link
        #y["waktu"] = waktu.text
        return y

def tampilkan_data(result):
        if result is None:
            return 'pass'
        print('Berita Terbaru CNN Indonesia')
        print(f'{result["judul"]}')
        print(f'{result["link"]}')
        #print(f'{result["waktu"]}')




