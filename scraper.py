from bs4 import BeautifulSoup

URL = "https://www.urbandictionary.com/define.php?term="
term = input("Enter a term:")
URL += term
print(URL)