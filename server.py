import multiprocessing
import uvicorn
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
import subprocess
import db

app = FastAPI()

@app.get("/setup/getconf")
def getConf():
    print(0)
    return db.read_conf()

@app.get('/setup/settoken')
def setToken(token: str):
    return db.upd_hftoken(token)

@app.get("/setup/settokenold")
def setToken():
    print('set token')
    process = subprocess.run(["./shell/set_token.sh"], capture_output=True, text=True)
    if(process.stderr): 
        return JSONResponse(content={"status": 0}, status_code=400)
    if(process.returncode == 0):
        return JSONResponse(content={"status": 1})
    
app.mount('/', StaticFiles(directory='dist', html=True), name='static')

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(content={"message": "No Match at all"}, status_code=404)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    uvicorn.run('server:app', host="0.0.0.0", port=8000, workers=2)
