import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
url = 'https://store.steampowered.com/games/#p=0&tab=NewReleases'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
new_releases = soup.find('div', attrs={'id':'NewReleasesRows'})
newReleaseContents = soup.findAll('a', attrs={'class':'tab_item'})

for newReleaseContent in newReleaseContents:
    imageUrl = newReleaseContent.find('img', attrs={'class':'tab_item_cap_img'})['src']
    titles = newReleaseContent.find('div', attrs={'class':'tab_item_name'}).text
    response = requests.get(imageUrl, headers=headers, stream=True)
    fileName = imageUrl.split("/")[-1].split("?")[0]
    ext = fileName[-4:]
    if response.ok:
        with open('images/' + re.sub(r'(?u)[^-\w.]', '_', titles) + ext, 'wb') as a:
            a.write(response.content)