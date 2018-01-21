import pymongo

# Connection to MongoDB - PersonDatabase - Users collection
conn=pymongo.MongoClient('localhost', 27017)
db = conn.PersonDatabase
collection = db.Users

# Inserting into Users collection
doc = {"FirstName":"John","LastName":"Doe","Age":22}
collection.insert(doc)

# Find records from Users collecion
collection.find({"FirstName":"John"})

# Thomas Boccinfuso - www.tboccinfuso.com / www.twitter.com/BoccinfusoT
