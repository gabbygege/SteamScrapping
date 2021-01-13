import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def top_sellers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
    }
    url = 'https://store.steampowered.com/games/#p=0&tab=TopSellers'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    top_sellers = soup.findAll('a', attrs={'class': 'tab_item'})
    return render_template('grid_template.html', top_sellers=top_sellers)
if __name__ == '__main__':
    app.run(debug=True)