# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymongo
import sys

MONGODB_URL = "mongodb+srv://cerenna0124:840124@cerenna.vxqr3gt.mongodb.net/?retryWrites=true&w=majority&appName=Cerenna"
client = pymongo.MongoClient(MONGODB_URL)
db = client['MongoClient']
col = db['Database']
cursor=col.find({})
go_next=False
for doc in cursor:
    if '我起床了' in doc['events'][0]['message']['text']:
        go_next=True
        
if go_next==False:
    sys.exit(0)
