import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import inquirer
import countySearch

session = HTMLSession()
URL = 'https://library.municode.com/'
headers = {"user-agent":"Mozilla/5.0"}
page = session.get(URL, headers=headers)
page.html.render(sleep = 3)
print("session header: ", page.request.headers)
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36

soup = BeautifulSoup(page.html.html, 'html.parser')
states_elements_container = soup.find_all('div', class_='container-fluid')[1]
#print("states list: ", states_container)

state_elements = states_elements_container.find_all('li')
#print("states count ", len(states))
#print("states list: ", states)
stateDict = {}
for state_element in state_elements:
  state = state_element.text.strip()
  link = state_element.find("a")["href"]
  stateDict[state] = link

# for x in stateDict:
#   print(x + " : " + stateDict[x])

questions = [
  inquirer.List('state',
                message="Please select a state to search:",
              #  choices=stateDict.keys(),
              choices=["Virginia"],)
]
#state user selected
answers = inquirer.prompt(questions)
print(answers['state'])
for x in stateDict:
  if(answers['state'] == x): 
    #search for a list of counties in the selected state
    countySearch.county(stateDict[x])    



  