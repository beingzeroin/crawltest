"""Remove the comment in the Spider.py line number 48"""
from bs4 import BeautifulSoup as soup
import requests
from pymongo import MongoClient
import datetime
from domain import *

class programiz:
    @staticmethod
    def extract_code(url):
        try:
            langArray = ['css', 'c', 'sql', 'xml', 'cpp', 'perl', 'delphi', 'php', 'csharp', 'bash', 'plain', 'java', 'wf',
                    'python', 'python3', 'jscript', 'r', 'kotlin']
            lang = url.split('/')[3].split('-')[0]
            if lang in langArray:
                try:
                    conn = MongoClient()
                    print('connected Succesfully')
                except:
                    print('Couldnt connect')
                db = conn.code
                collection = db.programiz
                page = requests.get(url)
                page = soup(page.content, "html.parser")
                content = page.findAll('pre')
                code = ""
                title = page.findAll('h1')
                title = title[0].text
                now = datetime.datetime.now()
                date = str(datetime.date.today())
                time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                domain = get_domain_name(url).split('.')[0]
                for con in content:
                    attr = con.code
                    if attr is not None:
                        code = con.text
                        collection.insert({'Title': title, 'Language': lang, 'code': code, 'Domain': domain, 'URL': url,
                                           'log-type': 'Insert', 'Date': date, 'Time': time})
                        print('Inserted')

        except :
            print('wrong')
