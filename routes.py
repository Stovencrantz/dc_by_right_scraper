import requests
import pprint

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
  
