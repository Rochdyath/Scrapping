import requests
from bs4 import BeautifulSoup

class HTTP_Client():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
            ]
        self.max_wait = 10

    def get_req_content(self, url):
        for user_agent in self.user_agents:
            header = {
                'User-Agent': user_agent
            }
            res = requests.get(url, headers=header, timeout=self.max_wait)
            if (res.status_code != 200):
                return None
            return(res.content)
    
    def get_req_text(self, url):
        for user_agent in self.user_agents:
            header = {
                'User-Agent': user_agent
            }
            res = requests.get(url, headers=header, timeout=self.max_wait)
            if (res.status_code != 200):
                return None
            return(res.text)
        
    
    def get_req_soup(self, url):
        for user_agent in self.user_agents:
            header = {
                'User-Agent': user_agent
            }
            res = requests.get(url, headers=header, timeout=self.max_wait)
            if (res.status_code != 200):
                continue
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
        return None


client = HTTP_Client()


## Exo 1
# url = 'https://www.ynov.com'
# text = client.get_req_text(url)
# print(text[0:1000])


## Exo 2
# url = 'https://www.ynov.com'
# soup = client.get_req_soup(url)

# H1_list = soup.find_all("H1")
# for h1 in H1_list:
    # print(h1)

# img_list = soup.find_all("img")
# for img in img_list:
#     try:
#         print(img['src'])
#     except:
#         continue

# a_list = soup.find_all("a", href=True)
# print(a_list[0])

# p_list = soup.find_all("p")
# for p in p_list:
#     print(p.get_text())


## Exo final
def get_url(article):
    url = article.find('a', href=True)
    if url != None:
        return url['href']
    return None

def get_title(article):
    title = article.find('h2')
    if title != None:
        return title.get_text()
    return None

def get_texte(article):
    texte = article.find('p')
    if texte != None:
        return texte.get_text()
    return None

def get_categories(url):
    categories = []
    soup = client.get_req_soup(url)
    if soup == None: return None
    span = soup.select('span.fig-breadcrumb__text')
    if span != None:
        for s in span:
            t = s.get_text()
            if t != 'Accueil': categories.append(t)
        return categories
    return None


def get_article_description(article):
    description = {}
    description['url'] = get_url(article)
    description['titre'] = get_title(article)
    description['texte'] = get_texte(article)
    description['catégorie'] = get_categories(description['url'])
    return description

url = 'https://www.lefigaro.fr/'
soup = client.get_req_soup(url)
articles = soup.find_all('article')
res = []

for article in articles:
    res.append(get_article_description(article))

for item in res:
    print(item)
