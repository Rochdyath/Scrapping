import requests
from bs4 import BeautifulSoup

url = 'https://www.ynov.com'

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
                print(res.status_code, res.text)
                continue
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
        return None


client = HTTP_Client()


## Exo 1
# text = client.get_req_text(url)
# print(text[0:1000])


## Exo 2
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
url = 'https://www.lefigaro.fr/culture'
soup = client.get_req_soup(url)
articles = soup.find_all('article')
res = []

for article in articles:
    description = {}
    description['url'] = article.find('a', href=True)['href']
    description['title'] = article.find('h2').get_text()
    description['texte'] = article.find('p').get_text()
    res.append(description)
    break

print(res)
