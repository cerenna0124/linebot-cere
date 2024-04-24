# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymongo
MONGODB_URL = "mongodb+srv://cerenna0124:840124@cerenna.vxqr3gt.mongodb.net/?retryWrites=true&w=majority&appName=Cerenna"
client = pymongo.MongoClient(MONGODB_URL)
db = client['MongoClient']
col = db['Database']
cursor=col.find({})
for doc in cursor:
    if '我起床了' in doc['events'][0]['message']['text']:
        print('你起床了!')
