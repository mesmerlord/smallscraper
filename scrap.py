import csv
import pandas as pd
import random
import cloudscraper
import requests
import string
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class Scraper():
    def __init__(self,requestType=None,prox = None):
        
        if requestType=="cloud":
            self.request = cloudscraper.create_scraper()   
        else:
            self.request = requests.Session()
        if prox:
            try:
                prox1 = pd.read_csv(prox)
                self.proxyList = prox1.values.tolist()
            except OSError:
                print("No such file found on that file path")
            except:
                print("not sure what went wrong")
    def getResponse(self,link,proxySupport=None,header=None):
        if "http://" or "https://" not in link:
            link = "https://"+link
        if proxySupport == "proxy" and self.proxyList:
            splitprox = random.choice(self.proxyList)[0].split(":")
            proxyy = f'http://{splitprox[2]}:{splitprox[3]}@{splitprox[0]}:{splitprox[1]}'
            response = self.request.get(link, headers=header,proxies = {'http':proxyy, 'https':proxyy})
            
        else:
            response = self.request.get(link, headers=header)
        return response


