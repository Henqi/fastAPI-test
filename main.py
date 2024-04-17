from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def main_route():
    return {"message": "Täsä mä ole!"}


@app.get("/roottori")
async def roottori():
    return {"message": "Ei ole nablaa täällä..."}
