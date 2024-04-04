import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import inquirer
import muniSearch

def county(URL): 
  print("url passed: ", URL)
  testURL = 'https://library.municode.com/va'
  session = HTMLSession()
  #page = session.get(URL)
  headers = {"user-agent":"Mozilla/5.0"}
  page = session.get(URL, headers=headers)  
  page.html.render(sleep = 3)
  soup = BeautifulSoup(page.html.html, 'html.parser')
  print("session header: ", page.request.headers)


  county_elements_container = soup.find_all('div', class_='container-fluid')[1]
  county_elements = county_elements_container.find_all('li')

  countyDict = {}

  for county_element in county_elements:
    county = county_element.text.strip()
    link = county_element.find("a")["href"]
    countyDict[county] = link

  # for x in countyDict:
  #   print(x + " : " + countyDict[x])

  questions = [inquirer.List('county',
              message="Please select a county to search:",
              choices=["Prince William County"]
              #choices=countyDict.keys()
              ,)
]
  #county user selected
  answers = inquirer.prompt(questions)
  print(answers['county'])
  for x in countyDict:
    if(answers['county'] == x): 
      #search for a list of municipalities in the selected county
      muniSearch.muni(countyDict[x]) 
