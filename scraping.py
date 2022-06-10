#!/usr/bin/python

##################
#  scraping.py
#  Name : Brian kyalo
#  Date : 23 / 5 / 20
###################


import requests 
from bs4 import BeautifulSoup as bs

user_name = "Brian Kyalo" #input("enter the user Name ")
url = "https://github.com" + user_name #input("Enter site Url")
results= requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})
print(profile_pic)
