from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myUrl= "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uClient = uReq(myUrl)
htmlPage = uClient.read()
uClient.close()
pageSoup = soup(htmlPage, "html.parser")

containers = pageSoup.findAll("div", {"class" : "_13oc-S"})
# print(len(containers))
container = containers[0]
# print(soup.prettify(container))
print(container.div.img["alt"])
# print(container.div.)
