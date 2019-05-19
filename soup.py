"""Remove the comment in the Spider.py line number 46"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from pymongo import MongoClient

class geeksforgeeks:
    @staticmethod
    def extract_code(url):
        try:
            try:
                conn = MongoClient()
                print('connected Succesfully')
            except:
                print('Couldnt connect')
            db = conn.code
            collection = db.mycode
            url = url.replace(" ","")
            uClient = uReq(url)
            source_code = uClient.read()
            page= soup(source_code,"html.parser")
            content = page.findAll('pre')
            for con in content:
                attr = con.get('class')
                if attr is not None:
                    title = url.split('/')
                    title = title[-2].replace('-', ' ')
                    lang = attr[1]
                    lang = str(lang)
                    lang = lang.replace(";","")
                    lang = lang.replace(" ","")
                    code = con.text
                    collection.insert({'title': title, 'lang': lang, 'code': code})
        except Exception as e:
            print('worng')
#extract_code(str(arul[0]))

