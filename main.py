import requests
import inquirer
import pprint
import time
# API for state list - https://api.municode.com/States/
# API for County list - https://api.municode.com/Clients/stateAbbr?stateAbbr=va
# API for Client Content - https://api.municode.com/ClientContent/5478
# API for Jobs - https://api.municode.com/Jobs/latest/14114
# API for Code of Ordinances TOC - https://api.municode.com/codesToc?jobId=450310&productId=14114
# API for TOC Contents - https://api.municode.com/codesToc/children?jobId=450310&nodeId=CH1GEPR&productId=14114
# API for last child of TOC Contents - https://api.municode.com/CodesContent?jobId=450310&nodeId=CH1GEPR_S1-1HOCODECI&productId=14114

pp = pprint.PrettyPrinter(indent=4)

def getAPI(URL):
  results = requests.get(URL)
  return results

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

stateDict = {}
for index in r.json():
  stateName = index['StateName']
  stateAbbr = index['StateAbbreviation']
  stateDict[stateAbbr] = stateName


# STEP 2 - Select county and get ${clientId} from https://api.municode.com/Clients/stateAbbr?stateAbbr=${stateAbbr}
def getCounty(stateAbbr):
  URL = f'https://api.municode.com/Clients/stateAbbr?stateAbbr={stateAbbr}'
  print(URL)
  r = requests.get(URL)
  #pp.pprint(r.json())

  for client in r.json():
    pp.pprint(client)
    # print(f"{client['ClientName']}  : {client['ClientID']}")
    # clientDict['client'] = client['ClientName']
    clientDict = {
    'stateAbbr' : stateAbbr,
    'ClientId' : client['ClientID'],
    'productId' : '',
    'jobId' : '',
    'nodeId' : '',
    'search' : {
      'terms' : '',
      'results' : '',
      'link' : ''
    }
  }
    locationDict[client['ClientName']] = clientDict

# limiting loop for development, remove index on prod
# index=0
# for key in stateDict:
#   if key==3:
#     break
#   getCounty(key) 
#   index+=1
#   time.sleep(1)  
for key in stateDict:
  if key == 'VA':
    getCounty(key)
pp.pprint(locationDict)
print(len(locationDict))
# STEP 3 - Get ${productId} from https://api.municode.com/ClientContent/{clientId}
# STEP 4 - Get ${jobId} from https://api.municode.com/Jobs/latest/{productId}
# STEP 5 - Get list of TOC children ${tocNodeId} from https://api.municode.com/codesToc?jobId={jobId}&productId={productId}
# STEP 6 - Get list of Child Nodes ${childNodeId} from https://api.municode.com/codesToc/children?jobId={jobId}&nodeId={nodeId}&productId={productId}
# STEP 7 - Get text content of final child node from https://api.municode.com/CodesContent?jobId={jobId}&nodeId={nodeId}&productId={productId}
