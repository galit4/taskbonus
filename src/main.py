from fastapi import FastAPI
from api import info, getnew, getknown, getkey, getall, initdb
#імпортуєм фастапі та модулі з ендпоінтами

app = FastAPI()#робимо еземпляр класу для зручності
app.include_router(info.router)#додаємо роутери з кожним ендпоінтом
app.include_router(getall.router)
app.include_router(getnew.router)
app.include_router(getknown.router)
app.include_router(getkey.router)
app.include_router(initdb.router)
