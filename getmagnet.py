import sys
import requests as req
from bs4 import BeautifulSoup
import re

#Function to format GB MB:
def formatB(string):
	word=[]
	for letter in string:
		word.append(letter)
	i=0
	while word[i]!='B':
		i+=1
	word.insert(i+1," ")
	del word[i-2]
	return "".join(word)

#Get information about torrent:
def getinfo(parent,counter):
	name=parent.find("td",{"class":"coll-1 name"}).get_text()
	seeders=parent.find("td",{"class":"coll-2"}).get_text()
	size=formatB(parent.find("td",{"class":"coll-4"}).get_text())
	print(str(counter) + ")" + " "*3 + size + " "*5 + name)
	
def Main():
	#Search
	try:
		term=input("Search for:").split()
	except KeyboardInterrupt:
		sys.exit(4)
	term="+".join(term) 
	#Create BS object
	link="https://1337x.to/search/" + term + "/1/"
	html=None
	html=req.get(link,headers={"User-Agent":"Mozilla/5.0"})
	if html is None:
		sys.exit(4)
	bsObj=BeautifulSoup(html.content,"html.parser")
	
	#Get torrent table
	tablerows=bsObj.findAll("tr")
	if len(tablerows) == 0:
		sys.exit(5)
	del tablerows[0]
	counter=1
	for tablerow in tablerows:
		getinfo(tablerow,counter)
		counter+=1
	try:
		counter=int(input("Select torrent:"))
	except (ValueError,KeyboardInterrupt):
		sys.exit(4)
	link="https://1337x.to" + tablerows[counter-1].find("td",{"class":"coll-1"}).a.next_sibling['href']

	#name=tablerows[counter].find("td",{"class":"coll-1 name"}).get_text()
	#Switch to selected torrent
	html=None
	html=req.get(link,headers={"User-Agent":"Mozilla/5.0"})
	if html is None:
		sys.exit(4)
	bsObj=BeautifulSoup(html.content,"html.parser")
	magnet=bsObj.find("a",href=re.compile("magnet"))['href']

	#Write magnet link to file
	file=open("magnet.txt","w+")
	file.write(magnet)
	#file=open("tname.txt","w+")
	#file.write(name)
	file.close()


Main()
