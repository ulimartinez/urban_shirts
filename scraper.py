from bs4 import BeautifulSoup
import requests
import re

while(True):
    URL = 'https://www.urbandictionary.com/define.php?term='
    print('\n')
    term = input('Enter a term: ')
    URL += term
    space = URL.replace(' ', '%20')
    print(space)

    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')
    definitions = soup.find('div', {'class': 'def-panel'})
    first_def = definitions.find('div', {'class': 'meaning'}).findAll('a')

    for w in first_def:
        clean = re.compile('<.*?>')
        word = re.sub(clean,'',w.text)
        print(word)


