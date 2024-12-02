from fastapi import APIRouter
import json
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

#для зручності виносим змінні
ES_INDEX = "underdefense_index"
API_KEY = "d3ZqSGlKTUJJQ0R0aU1pNTkxSEo6UnJtaGNrSWhRcWFPYVQ2TTFoclR0Zw=="
URL = "https://e269f958dd0d49d1ab5cc95576547374.us-central1.gcp.cloud.es.io:443"
client = Elasticsearch(
    URL, 
    api_key=API_KEY
)
def save(content): 
    doc = { "output": content} 
    client.index(index="outputsave", document=doc)
#робимо екземляр класу 
router = APIRouter()
@router.get("/get/new")
def getting():
    #відкриваєм файл та зберігаємо вміст
        response = client.get(index=ES_INDEX,id="jsonfile")
        content = response["_source"]
        output = []#пустий словник для подальшого ретурну

        #визначаємо 1000 днів як максимум старості цве
        for i in range(0, 1000):
            for cve in content["vulnerabilities"]: 
                #визначаємо поріг часу та форматуємо його для порівняння     
                startdate = str(datetime.now()-timedelta(days=i))
                startdate = startdate.split(" ")
                startdate = startdate[0]
                #зберігаємо найновіші цве
                if cve["dateAdded"] == startdate:
                    output.append(cve)
                #обмежуєм по кількості
                if len(output) == 10:
                    save(output)
                    return output
        save(output)               
        return output
            