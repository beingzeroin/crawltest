from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "https://www.geeksforgeeks.org/number-shortest-paths-unweighted-directed-graph/"
uClient = uReq(url)
source_code = uClient.read()
page= soup(source_code,"html.parser")
content = page.findAll('div',{'id':'main'})
print(content[0].div.div)