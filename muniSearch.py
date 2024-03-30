import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import inquirer

def muni(URL):
  print("url passed: ", URL)

  session = HTMLSession()
  page = session.get(URL)
  page.html.render(sleep=5)


  soup = BeautifulSoup(page.html.html, "html.parser")

  codes_container_element = soup.find(id='content')
  ui_view = codes_container_element.find('ui-view')
  zones_element = ui_view.find('div', class_='zones')
  toc_element = zones_element.find(id='toc')
  #toc_section_element = zone_body_element.find(id='toc')
  # toc_zone_body_element = toc_section_element.find('div', class_='toc-zone-body')
  # toc_wrapper_element = zone_body_element.find(id='genToc')

  print(zones_element)

