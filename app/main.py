
# from fastapi import FastAPI
# app = FastAPI()


# @app.get("/hello")
# async def hello():
#     return {"hello" : "world"}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

############################################################################################################################
############################################################################################################################
############################################################################################################################
import requests
import json
import uvicorn
import redis
from fastapi import FastAPI
import uuid

app = FastAPI()
rd = redis.Redis(host = "redis", port = 6379, password="changeme")

@app.get("/redis_test")
def redis_test():
    result = (rd.ping())

    return {
        "result" : result
    }
@app.get("/")
def root():
    return {"hello world": "access_success"}

@app.get("/hello")
def hello():
    return {"nginx":"working"}

@app.get("/{user_name}")
def read_fish(user_name:str):
    cache = rd.get(user_name)
    if cache:
        print("chach hit")
        return {"user_name" : cache}
    else:
        print("cache miss")
        sessionid = uuid.uuid4()
        sessionid= str(sessionid)
        rd.set(user_name, sessionid)
        rd.expire(user_name, 10)
        return {"user_name" : "no_data"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
