from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("victor.altamirano.izquierdo@gmail.com", "victor15", url="https://68266e00-2181-441d-b907-6682711542bc-bluemix.cloudant.com/")
client.connect()

databaseName = "Nueva"

myDatabase = client.create_database(databaseName)

if myDatabase.exists():
    print ("'{0}' successfully created.\n".format(databaseName))

sampleData = [
    [1, "one", "boiling", 100],
    [2, "two", "hot", 40],
    [3, "three", "warm", 20],
    [4, "four", "cold", 10],
    [5, "five", "freezing", 0]
]

# Create documents using the sample data.
# Go through each row in the array
for document in sampleData:
    # Retrieve the fields in each row.
    number = document[0]
    name = document[1]
    description = document[2]
    temperature = document[3]

    # Create a JSON document that represents
    # all the data in the row.
    jsonDocument = {
        "numberField": number,
        "nameField": name,
        "descriptionField": description,
        "temperatureField": temperature
    }

    # Create a document using the Database API.
    newDocument = myDatabase.create_document(jsonDocument)

    # Check that the document exists in the database.
    if newDocument.exists():
        print ("Document '{0}' successfully created.".format(number))

result_collection = Result(myDatabase.all_docs)

print ("Retrieved minimal document:\n{0}\n".format(result_collection[0]))

result_collection = Result(myDatabase.all_docs, include_docs=True)
print ("Retrieved full document:\n{0}\n".format(result_collection[0]))

end_point = '{0}/{1}'.format("<url>", databaseName + "/_all_docs")
params = {'include_docs': 'true'}
response = client.r_session.get(end_point, params=params)
print ("{0}\n".format(response.json()))


try :
    client.delete_database(databaseName)
except CloudantException:
    print ("There was a problem deleting '{0}'.\n".format(databaseName))
else:
    print ("'{0}' successfully deleted.\n".format(databaseName))

client.disconnect()