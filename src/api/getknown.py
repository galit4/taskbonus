from fastapi import APIRouter
import json
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Get new cve"])
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
@router.get("/get/known")
def getting():
    #відкриваєм файл та зберігаємо вміст
    response = client.get(index=ES_INDEX,id="jsonfile")
    #достпаємся за ключем до нашого файлу
    content = response["_source"]
    output = []#пустий словник для подальшого ретурну


    for cve in content["vulnerabilities"]:         
        if cve["knownRansomwareCampaignUse"] == "Known":
            output.append(cve)
            #обмеження по довжині
            if len(output) == 10:
                #зберігаємо в індекс
                save(output)
                return output
        