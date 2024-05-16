import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4)


def getAPI(URL):
  results = requests.get(URL)
  return results

def getProduct(URL):
  print("our url: ", URL)
  r = getAPI(URL)
  productId = r.json()['codes'][0]['productId']
  print('routes productId: ', productId)
  return productId
  
def getJob(URL):
  print("Job Url: ", URL)
  r = getAPI(URL)
  jobId = r.json()['Id']
  return jobId

def getToc(URL):
  print('TOC url: ', URL)
  r = getAPI(URL)
  # Create a dictionary for each TOC index and capture the key,value pair for Id, Heading, and HasChildren
  tocList = []
  for code in r.json()['Children']:
    tempDict = {'id':"", 'hasChildren':""}
    tempDict['id'] = code['Id']
    tempDict['heading'] = code['Heading']
    tempDict['hasChildren'] = code["HasChildren"]
    tocList.append(tempDict)
 # pp.pprint(tocList)
  return tocList

def getCodeContent(URL):
  r = getAPI(URL)
  print(f"{r.status_code} : {URL}")
  content = r.json()['Docs'][0]['Content']
  soup = BeautifulSoup(content, 'html.parser')
  print(soup.prettify())
  #pp.pprint(content)
  

def getNodes(URL):
  r = getAPI(URL)
  print(f"{r.status_code} : {URL}")