import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
database = client["neurolabDB"]
collection = database["products"]

data = {
    "companyName": "iNeuron",
    "product": "Affordable AI",
    "courseOffered": "Machine Learning with Deployment"
}

record = collection.insert_one(data)
print("Inserted Record ID:", record.inserted_id)

all_records = collection.find()

print("\nAll Records in Collection:")
for idx, rec in enumerate(all_records):
    print(f"{idx+1}: {rec}")