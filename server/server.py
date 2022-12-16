from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from asyncio.windows_events import NULL
import datetime, json, os, logging, uuid, uvicorn
from fastapi import FastAPI, Body, Request
# from aiohttp.web import Response
# from fastapi.requests import BaseRequest
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="A7 Laptop Backend", version="0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("== Now Running A7 Laptop Server... ==")
print("Running from:", os.getcwd())

@app.get("/")
async def root():
    return {"message": str(datetime.datetime.now()) +" | "+ "A7 Laptop Server running !"}

@app.get("/get_status")
async def root():
    return {"message": str(datetime.datetime.now()) +" | "+ "A7 Laptop Server running !"}


from starlette.responses import FileResponse
@app.get("/ctpc")
def read_status():
    return FileResponse("storage/app-release.apk", media_type='application/octet-stream',filename="CTPC.apk")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=5000, reload=True)