import string
import time
import traceback

import pymysql
import requests
import re

from lxml import etree
import random

from bs4 import BeautifulSoup
from flask import json

def get_tencent_data():
    url_bean = 'https://movie.douban.com/subject/26752088/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }

    text=requests.get(url=url_bean,headers=headers).text
    ex=' <span class="pl">制片国家/地区:</span> (.*?)<br/>'
    test=re.findall(ex,text,re.S)
    ex2='<span class="pl">语言:</span> (.*?)<br/>'
    test = re.findall(ex2, text, re.S)
    summary = test[0].replace(" / ", " ")
    print(summary)


if __name__ == "__main__":
   get_tencent_data()