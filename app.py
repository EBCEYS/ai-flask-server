"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#from crypt import methods
from types import SimpleNamespace
import requests
import json
from DataSetClasses import ClevelandDataSet
from flask import Flask, request

from ActionResponse import ActionResponse
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

f = open("appsettings.json", "r")

config = json.load(f)
print("Loaded configuration:", config)

def LoadStartSystem():
    if __name__ == '__main__':
        import os
        HOST = os.environ.get('SERVER_HOST', 'localhost')
        PORT = int(config["StartingPort"])
        app.run(host=HOST, port=PORT)


def DataSetFromRequest(dataSet):
    dstype = dataSet["DataSetType"]
    if dstype == "Cleveland":
        cleveland = ClevelandDataSet(dataSet)
        print("Data is cleveland")
        return cleveland
    else:
        print("Data is default")
        return {}

@app.route('/ping', methods=["GET"])
def Ping():
    print("Request is /ping")
    answer = "pong"
    print("Answer is ", answer)
    return "pong", 200

@app.route('/SVM', methods=["POST"])
def Svm():
    #try:
        data = request.data
        print("Request is /SVM with data", data)
        parsedData = DataSetFromRequest(data)
        answerObj = ActionResponse("OK", 0.0).ToJson()
        print("Answer is ", answerObj)
        return answerObj, 200
    #except Exception:
    #    print(Exception)
    #return ActionResponse("ERROR", 0.0).ToJson(), 415


#HttpRequests:
def PostRequest(method, json):
    api_url = str(config['ApiIp']) + "/" + method
    print("Post request to: ", api_url, " with data: ", json)
    header =  {"Content-Type":"application/json"}
    response = requests.post(api_url, json = json, headers = header)
    if response.status_code == 200:
        return response.json()
    else:
        return "{}";

def GetRequest(method):
    api_url = str(config['ApiIp']) + "/" + method
    print("Get request to: ", api_url)
    header =  {"Content-Type":"application/json"}
    response = requests.get(api_url, headers = header)
    if response.status_code == 200:
        return response.json()
    else:
        return "{}";


LoadStartSystem()

#TODO: алгоритмы для которых нужны контроллеры
#        Cleveland,
#        RandomForest,
#        SVM, +
#        BILSTM,
#        NAIVEBAYES
