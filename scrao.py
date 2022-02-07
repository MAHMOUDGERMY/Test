print("126")
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

result = requests.get("https://www.agedcareguide.com.au/search/in-home-care/aus?page=1")

src = result.content

soup = BeautifulSoup(src , "lxml")

files = soup.find_all("div"  , {"class" : "search-resul profile-card tw-mb-6"})

print(files)