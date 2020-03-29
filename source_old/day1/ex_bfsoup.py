
from bs4 import BeautifulSoup
import os

os.getcwd()
with open("./source/day1/example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# print(soup)

all_ps=soup.find_all("p")
print(all_ps)



