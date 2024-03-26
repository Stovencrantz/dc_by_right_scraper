import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
URL = 'https://library.municode.com/'
page = session.get(URL)
page.html.render()
#print(page.html.html)

soup = BeautifulSoup(page.html.html, 'html.parser')
states_container = soup.find_all('div', class_='container-fluid')[1]
#print("states list: ", states_container)

states = states_container.find_all('li')
#print("states count ", len(states))
#print("states list: ", states)
stateDict = {}
for state in states:
  site = state.text.strip('\n')
  link = state.find("a")["href"]
  stateDict[site] = link

for x in stateDict:
  print(x + " : " + stateDict[x])

