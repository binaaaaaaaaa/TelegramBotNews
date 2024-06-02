import requests
from bs4 import BeautifulSoup

def getnew():
    titles = []
    r = requests.get('https://tapchibitcoin.io/huong-dan')
    soup = BeautifulSoup(r.text, 'html.parser')
    mydiv = soup.find_all('h3', {'class': 'entry-title td-module-title'})
    for new in mydiv:
        title = new.a.get('title')
        href = new.a.get('href')
        titles.append((title, href))
    return titles

# Test function (Optional)
if __name__ == "__main__":
    news = getnew()
    for title, link in news:
        print(f'Title: {title}\nLink: {link}')
