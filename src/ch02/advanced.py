from urllib.request import urlopen
from bs4 import BeautifulSoup

def printList(tags) :
    print("start=====================================")
    for tag in tags:
        print(tag.get_text())

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class" : "green"})
printList(nameList)

spanList = bsObj.findAll("span", {"class" : {"green", "red"}});
printList(spanList)

textList = bsObj.findAll(text="the prince")
print(len(textList))

allText = bsObj.findAll(id="text")
print(allText[0].get_text)