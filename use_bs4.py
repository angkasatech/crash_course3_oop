import requests
from bs4 import BeautifulSoup

url = 'https://detik.com' #request ambil data detikcom

try:
    response = requests.get(url)
    if response.status_code == 200: #cek status code-nya
        #print('Success!', response)
        #print(f'Success! {response}')
        print(f'Success! Response {response.status_code}') #tampilkan isi/code-nya
        #print(f'Content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan {url}')
        #print(f'Title: {soup.title}')
        print(f'Title: {soup.title.string}')
    else:
        print((f'Woops, there is requests failure {response.status_code}'))

except Exception as e:
    #print('There is an error', e)
    print(f'There is an error {e}')
print('Program ended')