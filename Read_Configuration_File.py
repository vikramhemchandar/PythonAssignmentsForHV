"""
In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
●       The program should read a configuration file (you can provide them with a sample configuration file).
●       It should extract specific key-value pairs from the configuration file.
●       The program should store the extracted information in a data structure (e.g., dictionary or list).
●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
●       Finally save the output file data as JSON data in the database.
●       Create a GET request to fetch this information.
Sample Configuration file: 
[Database]
host = localhost
port = 3306
username = admin
password = secret
 
[Server]
address = 192.168.0.1
port = 8080
 
Sample Output: 
Configuration File Parser Results:
Database:
- host: localhost
- port: 3306
- username: admin
- password: secret
 
Server:
- address: 192.168.0.1
- port: 8080 
"""
import configparser
from flask import Flask, jsonify, request
from pymongo import MongoClient
import webbrowser

#To Read the file and converting the data into a Dictionary  
def read_file(file_path):

    #Try block to handle errors gracefully
    try:
        data = {}
        config = configparser.ConfigParser()
        config.read(file_path)

        #This throws an exception if the configuration file is empty or invalid   
        if not config.sections():
            raise Exception("Configuration file is empty or invalid.")
        
        #Convert the configuration file into a dictionary
        for section in config.sections():
            data[section] = {}
            for key, value in config.items(section):
                data[section][key] = value
                
    #except blocks to print the errors
    except FileNotFoundError:
        print("File not found")
    except Exception as exception:
        print("Exception raised : ", exception)
    return data


#save the configuration data to a Mongo DB
def save_to_database(data):

    #Mongo DB Details
    client = MongoClient("mongodb+srv://vikram_DB:FsGnNq5GNa6idbot@vikramhemchandar.rtgw4pn.mongodb.net/")
    database = client["pythonfordevops"]
    collection = database["config_data"]

    try:
        # Insert new document on the given DB and Collection
        result = collection.insert_one(data)
        print(f"Data inserted with document ID: {result.inserted_id}")

    except Exception as e:
        print(f"Error inserting into MongoDB: {e}")

app = Flask("__name__")

#This is optional. Welcome page with a hyper link to Get the Config Data.
@app.route("/")
def default_page():
    print("This is the home page")
    return '''
        <h1>Welcome to Config Data Program</h1>
        <a href="/getConfigData">Get Config Data</a>
        '''

#To fetch the data from Mongo DB and print it in JSON format on web browser. 
@app.route("/getConfigData", methods=["GET"])
def get_config_data():
    client = MongoClient("mongodb+srv://vikram_DB:FsGnNq5GNa6idbot@vikramhemchandar.rtgw4pn.mongodb.net/")
    database = client["pythonfordevops"]
    collection = database["config_data"]

    document = collection.find_one(sort=[("_id", -1)])
    if document:
        # Remove MongoDB internal id before returning
        document.pop("_id", None)
        return jsonify(document)
    else:
        return jsonify({"error": "No configuration data found"}), 404

if __name__ == "__main__":    
    data = read_file("Configuration.txt")

    #Printing the data in the desired format
    if data:
        print("Configuration File Parser Results:")
        for section, values in data.items():
            print(f"{section}:")
            for key, val in values.items():
                print(f"- {key}: {val}")
    
    save_to_database(data)
    app.run(debug=True)

            

