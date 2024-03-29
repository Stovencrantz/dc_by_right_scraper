import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import inquirer

def muni(URL):
  print("url passed: ", URL)
