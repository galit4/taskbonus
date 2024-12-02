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
#створюєм клієнта і передаємо туди значення
client = Elasticsearch(
    URL, 
    api_key=API_KEY
    )
#функція для збереження в індекс
def save(content): 
    doc = { "output": content} 
    client.index(index="outputsave", document=doc)
@router.get("/get/")
def getting(key: str):
    #відкриваєм файл та зберігаємо вміст
    response = client.get(index=ES_INDEX,id="jsonfile")
    content = response["_source"]
    output = []#пустий словник для подальшого ретурну
    value = content.get("vulnerabilities")
    #перетворюєм cve в текст і додаєм його у список якщо у ньому є key
    for cve in value:
        if key in str(cve):
            #аппендим список та зберігаємо в індекс
            output.append(cve)
            save(output)
    return output
