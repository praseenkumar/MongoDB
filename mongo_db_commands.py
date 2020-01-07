# Mongo DB packages
import pymongo
from pymongo import MongoClient

#connect to mongoserver which is installed on port 27017 on local machine
connection = MongoClient('localhost', 27017)

#textsumm is the database name
db = connection.textsumm

#handle to text summary Collection in textsumm database
collection_name = db.textsumm

#insert a document into Mongo DB collection
val=collection_name.insert({
                    
            'identity':identity,
            'category':category_val,
            'summary':summary_val,
            'timestamp':timestamp,
            'predictedcategory':predicted_category,
            'source':source
     
            })

#fetch all the documents inside a collection
summarylist=collection_name.find()

#sort the documents inside collection from latest to oldest as per their creation timestamp
#-1 denotes descending order and +1 denotes ascending order
#'_id' is a key in each document of a mongodb collection which will be there by default it denotes the timestamp when the document is created.
collection_name.find().sort([('_id',-1)])

