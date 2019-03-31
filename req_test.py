#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = dogebyte
__date__ = 2019/2/24
"""

import re
import requests
import urllib.request
from bs4 import BeautifulSoup

rsp = requests.get('https://www.baidu.com/')
print(rsp)
soup = BeautifulSoup(rsp.text, 'html.parser')

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0')]
urllib.request.install_opener(opener)

for img in soup.find_all('img', src=re.compile(r'.*upload.*')):
    img_url = img['src']
    img_name = img['title']
    print(img_url)
    print(img_name)
    urllib.request.urlretrieve(img_url, r'f:\workspace\spider\images\%s' % img_name)
