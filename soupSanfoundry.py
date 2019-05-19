"""Remove the comment in the Spider.py line number 47"""
from bs4 import BeautifulSoup as soup
import requests
from pymongo import MongoClient
import datetime
from domain import *

class sanfoundry:
    @staticmethod
    def extract_code(url):
        try:
            langArray = ['css', 'c', 'sql', 'xml', 'cpp', 'perl', 'delphi', 'php', 'csharp', 'bash', 'plain', 'java',
                         'wf',
                         'python', 'python3', 'jscript', 'r', 'kotlin']
            title = url.split('/');
            title = title[-2]
            lang = title.split('-')[0];
            title = title.replace('-', ' ')
            if lang in langArray:
                try:
                    conn = MongoClient()
                    print('connected Succesfully')
                except:
                    print('Couldnt connect')
                db = conn.code
                collection = db.sanfoundry
                page = requests.get(url)
                page = soup(page.content, "html.parser")
                content = page.findAll('pre', {'class': "de1"})
                code = ""
                now = datetime.datetime.now()
                date = str(datetime.date.today())
                time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
                domain = get_domain_name(url).split('.')[0]
                for con in content:
                    attr = con.span
                    if attr is not None:
                        code += (con.text+"\n")
                collection.insert({'Title':title,'Language':lang,'code':code,'Domain' : domain,'URL' : url,'log-type':'Insert','Date':date,'Time':time})
                print('Inserted')
        except :
            print('wrong')
#domain
