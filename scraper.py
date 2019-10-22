from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.urbandictionary.com/define.php?term='
term = input('Enter a term: ')
URL += term
print(URL)

html = requests.get(URL).text

soup = BeautifulSoup(html, 'html.parser')
definitions = soup.find('div', {'class': 'def-panel'})
first_def = definitions.find('div', {'class': 'meaning'}).findAll('a')

for w in first_def:
    clean = re.compile('<.*?>')
    word = re.sub(clean,'',w.text)
    print(word)


