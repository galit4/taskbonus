from fastapi import APIRouter
#робимо екземляр класу та додаємо тег для зручності
router = APIRouter(tags=["Info"])
#вказуєм ендпоінт в декораторі, та ретюрним інфу у функції
@router.get("/info1")
def info_print():
    return {"Author": "Yurchyshyn Dmytro", 
            "ProgramDeskriprtion":"Simple FastApi example"}