import requests
import inquirer
import pprint
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
pp.pprint(r.json())


stateDict = {}
for index in r.json():
  stateName = index['StateName']
  stateAbbr = index['StateAbbreviation']
  stateDict[stateAbbr] = stateName
  # print(stateAbbr + " : " + stateName)
pp.pprint(stateDict)


for key in stateDict:
  print ("the key name is " + key + " and its value is " + stateDict[key])


questions = [
  inquirer.List('states',
                message="Please select a state to search:",
              #  choices=stateDict.values(),)
              choices=["Virginia"],)
]
answers = inquirer.prompt(questions)
print("You chose: ", answers['states'])

stateAbbr = ''
for key in stateDict:
  if (stateDict[key] == answers['states']):
    stateAbbr = key
    break
print("The abbreviation is: ", stateAbbr)


# STEP 2 - Select county and get ${clientId} from https://api.municode.com/Clients/stateAbbr?stateAbbr=${stateAbbr}
def getCounty(stateAbbr):
  URL = f'https://api.municode.com/Clients/stateAbbr?stateAbbr={stateAbbr}'
  print(URL)
  r = requests.get(URL)
  pp.pprint(r.json())

getCounty(stateAbbr)
   

# STEP 3 - Get ${productId} from https://api.municode.com/ClientContent/{clientId}
# STEP 4 - Get ${jobId} from https://api.municode.com/Jobs/latest/{productId}
# STEP 5 - Get list of TOC children ${tocNodeId} from https://api.municode.com/codesToc?jobId={jobId}&productId={productId}
# STEP 6 - Get list of Child Nodes ${childNodeId} from https://api.municode.com/codesToc/children?jobId={jobId}&nodeId={nodeId}&productId={productId}
# STEP 7 - Get text content of final child node from https://api.municode.com/CodesContent?jobId={jobId}&nodeId={nodeId}&productId={productId}
