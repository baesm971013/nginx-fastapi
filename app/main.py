
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

import uvicorn
import redis
from fastapi import FastAPI


app = FastAPI()


@app.get("/redis_test")
def redis_test():
    r = redis.Redis(host = "redis", port = 6379, password="changeme")
    result = (r.ping())

    return {
        "result" : result
    }


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}

@app.get("/hello")
def hello():
    return {"nginx":"working"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
