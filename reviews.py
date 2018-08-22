import requests
import time
from bs4 import BeautifulSoup
import  urllib.request as urllib2
import xml.etree.ElementTree as ET



def goodreads_review(book_id,start,stop,stats=False):
		reviews = 0
		start_time = time.time()
		api_key = 'ochCCR41mJswKwgdfkHQ4Q'
		secret = 'HO2trVBPsQtlEwsc3D9FdGILlwFf3KUecfW0OGMPxc'
		for id_number in range(start,stop):
				
			url_link = 'https://www.goodreads.com/review/show.xml?book_id=book_id&id='+str(id_number)+'&key='+str(api_key)
			r = requests.get(url_link)
			if r.status_code == 404: 
				print('skip')
			else:
				print(r.status_code)
				reviews = reviews + 1
				response = urllib2.urlopen(url_link).read()
				soup = BeautifulSoup(response,'lxml-xml')
				print(soup)
				with open("data.xml", "w") as f:
  					f.write(str(soup))
			if stats == True:
				end_time = time.time()
				print(str(end_time - start_time) +' seconds for goodreads_review')
				print('no. of reviews received: ' + str(reviews))
		else:
			print('We have completed the downloading the reviews')







