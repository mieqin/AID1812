#mongo_test1.py
from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)
db = conn.myfile

fs = gridfs.GridFS(db)
f = open('4.jpg','rb')

fs.put(f.read(),filename='mm.jpg')
conn.close()