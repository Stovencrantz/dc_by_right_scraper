import requests
import inquirer
import pprint
import time
from routes import getProduct, getAPI
# API for state list - https://api.municode.com/States/
# API for County list - https://api.municode.com/Clients/stateAbbr?stateAbbr=va
# API for Client Content - https://api.municode.com/ClientContent/5478
# API for Jobs - https://api.municode.com/Jobs/latest/14114
# API for Code of Ordinances TOC - https://api.municode.com/codesToc?jobId=450310&productId=14114
# API for TOC Contents - https://api.municode.com/codesToc/children?jobId=450310&nodeId=CH1GEPR&productId=14114
# API for last child of TOC Contents - https://api.municode.com/CodesContent?jobId=450310&nodeId=CH1GEPR_S1-1HOCODECI&productId=14114

pp = pprint.PrettyPrinter(indent=4)

# STEP 1 - Select state and get ${stateAbbr} from https://api.municode.com/States/
URL = "https://api.municode.com/States/"
headers = ""
r = getAPI(URL)
# Append to this dictionary so that we can loop through ALL code lines for each county for each state
# Add true/false flag for detecting of 'data center' or 'data processing' keywords
# Add link to be sent back to user
# This data is what we will pass in our dataframe at the end.

# locationDict = {
#   'clientName' : {
#     'stateAbbr' : "",
#     'ClientId' : '',
#     'productId' : '',
#     'jobId' : '',
#     'nodeId' : '',
#     'search' : {
#       'terms' : '',
#       'results' : '',
#       'link' : ''
#     }
#   }
# }

locationDict = {}
count = 0
stateDict = {}
for index in r.json():
  stateName = index['StateName']
  stateAbbr = index['StateAbbreviation']
  stateDict[stateAbbr] = stateName


# STEP 2 - Select county and get ${clientId} from https://api.municode.com/Clients/stateAbbr?stateAbbr=${stateAbbr}
def getCounty(stateAbbr):
  URL = f'https://api.municode.com/Clients/stateAbbr?stateAbbr={stateAbbr}'
  #print(URL)
  r = requests.get(URL)
  #pp.pprint(r.json())

  j = 0
  for client in r.json():
    clientDict = {
    'stateAbbr' : stateAbbr,
    'clientId' : client['ClientID'],
    'productId' : '',
    'jobId' : '',
    'nodeId' : '',
    'search' : {
      'terms' : '',
      'results' : '',
      'link' : ''
    }
  }
    clientName = client['ClientName']
    locationDict[clientName] = clientDict
    currentClient = locationDict[clientName]
    url = f"https://api.municode.com/ClientContent/{clientDict['clientId']}"
    currentClient['productId'] = getProduct(url)
    print('main productId: ', currentClient['productId'])
    j+=1
    if j==3:
      break
  print(locationDict)

# limiting loop for development, remove index on prod
# for key in stateDict:
#   if index==3:
#     break
#   getCounty(key) 
#   index+=1
#   time.sleep(1)  
j = 0
for key in stateDict:
  if key == 'VA':
    getCounty(key)
  
print(len(locationDict))

# STEP 3 - Get ${productId} from https://api.municode.com/ClientContent/{clientId}

# STEP 4 - Get ${jobId} from https://api.municode.com/Jobs/latest/{productId}
# STEP 5 - Get list of TOC children ${tocNodeId} from https://api.municode.com/codesToc?jobId={jobId}&productId={productId}
# STEP 6 - Get list of Child Nodes ${childNodeId} from https://api.municode.com/codesToc/children?jobId={jobId}&nodeId={nodeId}&productId={productId}
# STEP 7 - Get text content of final child node from https://api.municode.com/CodesContent?jobId={jobId}&nodeId={nodeId}&productId={productId}
