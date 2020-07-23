#!/usr/bin/env/ python3
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests
import re

def main():
    term = input('Enter a term: ')
    words = GetTerms(term)
    print(words)
    WriteToImage(term, words)

def GetTerms(term):

    URL = 'https://www.urbandictionary.com/define.php?term='
    URL += term

    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')
    definitions = soup.find('div', {'class': 'def-panel'})
    first_def = definitions.find('div', {'class': 'meaning'}).findAll('a')

    words = []
    for w in first_def:
        clean = re.compile('<.*?>')
        word = re.sub(clean,'',w.text)
        words.append(word)
    return words

def WriteToImage(term, words):
    im = Image.open("shirt.jpg")
    font = ImageFont.truetype('/usr/share/fonts/TTF/Koruri-Light.ttf', 90)
    font2 = ImageFont.truetype('/usr/share/fonts/TTF/Koruri-Light.ttf', 60)
    draw = ImageDraw.Draw(im)
    offset= 370 - ((len(term)//2) * 37)
    draw.text((offset,140), term, font=font, fill=(0,0,7))
    for i in range(min(len(words), 4)):
        w = (words[i][:16]) if len(words[i]) > 16 else words[i]
        draw.text((200, 290+(i*100)), w, font=font2, fill=(73,109,137))
    im.save("shirt_text.jpg")


if __name__ == "__main__":
    main()

