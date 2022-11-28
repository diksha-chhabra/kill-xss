import requests
from bs4 import BeautifulSoup
 
 
Target = input("Type your target URL...")
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
for link in soup.find_all('input'):
    print(link.get('href'))
