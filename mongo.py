from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.stu

myset = db.class4

#myset.insert({'name':'吴奇隆','King':"四爷"})

cursor = myset.find({},{'_id':0})

for i in cursor:
    print(i)

conn.close()