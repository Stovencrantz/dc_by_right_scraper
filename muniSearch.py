import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import inquirer
import pprint

def muni(URL):
  print("url passed: ", URL)
  apiURL = "https://api.municode.com/codesToc?jobId=450310&productId=14114"

  def testJSON(URL):
    session = HTMLSession()
    headers = {"user-agent":"Mozilla/5.0"}
    page = session.get(URL, headers=headers).json()
    pp = pprint.PrettyPrinter(indent=4)
  #  pp.pprint(page['Children'])
    jsonChildren = page['Children']
    for child in jsonChildren:
      pp.pprint(child)
      print(" ")

  def standard(URL): 
    session = HTMLSession()
    headers = {"user-agent":"Mozilla/5.0"}
    page = session.get(URL, headers=headers) 

    script = """
                console.log("hello world")
    """
    page.html.render(script=script, sleep=3)
    print("session header: ", page.request.headers)



    soup = BeautifulSoup(page.html.html, "html.parser")

    codes_container_element = soup.find(id='content')
    ui_view = codes_container_element.find('ui-view')
    zones_element = ui_view.find('div', class_='zones')
    section_elements = soup.find_all('sections')
    toc_button_element = zones_element.find(class_='container-fluid').find('button')
    #toc_section_element = zone_body_element.find(id='toc')
    # toc_zone_body_element = toc_section_element.find('div', class_='toc-zone-body')
    # toc_wrapper_element = zone_body_element.find(id='genToc')

    print(toc_button_element)

  # testJSON(apiURL)
  standard(URL)
