import json
from elasticsearch import Elasticsearch
from fastapi import APIRouter

#робимо екземпляр класу роутер, присвоюємо ендпоінт
router = APIRouter()
@router.get("/init-db")
def inniting():
    #ініціалізуємо змінні та створюємо клієнта з ними
    ES_INDEX = "underdefense_index"
    API_KEY = "d3ZqSGlKTUJJQ0R0aU1pNTkxSEo6UnJtaGNrSWhRcWFPYVQ2TTFoclR0Zw=="
    URL = "https://e269f958dd0d49d1ab5cc95576547374.us-central1.gcp.cloud.es.io:443"
    client = Elasticsearch(
        URL, 
        api_key=API_KEY
    )
    with open("/home/dmytro/Desktop/Code/underbonus/taskbonus/src/cve.json", "r") as file:
        content = json.load(file)
    {
   
    }
    try:#обробляєм помилку в разі наявності такої та записуємо файл у бд
        responce = client.create(index=ES_INDEX, id="jsonfile", body=content)
        return responce
    except Exception as e:
        return e

        