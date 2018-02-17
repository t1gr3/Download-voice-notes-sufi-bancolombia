#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import os
import time


url = 'http://34.208.68.190/audios'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html5lib")


for link in soup.findAll('a', {'href': re.compile('[0-9]{1,4}')}):

	l1 = link.get('href')

	os.mkdir(l1)

	ruta = os.getcwd() + '/' + l1

	os.chdir(ruta)


	url1 = 'http://34.208.68.190/audios' + '/' + l1

	resp1 = requests.get(url1)
	soup1 = BeautifulSoup(resp1.text, "html5lib")



	for link2 in soup1.findAll('a', {'href': re.compile('[0-9]{1,12}')}):

		l2 = link2.get('href')

		l3 = l2.replace('.mp3', '')


		phoneLists = open('phones.txt', 'a+')
		phoneLists.write(l3 + '\r\n')

		voiceNote = open(l2, 'wb')
		voiceNote.write(url1 + l2 + '\r\n')

		time.sleep(3)


	phoneLists.close()
	voiceNote.close()


	os.chdir('..')