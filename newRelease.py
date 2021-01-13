from uu import encode
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}

url = 'https://store.steampowered.com/games/#p=0&tab=NewReleases'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

new_releases = soup.findAll('a', attrs={'class':'tab_item'})
file = open('steam.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])

for new_release in new_releases:
    if(new_release.find('div', attrs={'class':'tab_item_name'}) != None):
        title = new_release.find('div', attrs={'class':'tab_item_name'}).text
    else:
        title=''
    if (new_release.find('div', attrs={'class': 'discount_final_price'}) != None):
        price = new_release.find('div', attrs={'class': 'discount_final_price'}).text
    else:
        price = ''
    if (new_release.find('div', attrs={'class': 'tab_item_top_tags'}) != None):
        tags = new_release.find('div', attrs={'class': 'tab_item_top_tags'}).text
    else:
        tags = ''
    file = open('steam.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tags])
    file.close()