import json

from fastapi import FastAPI
from starlette.responses import JSONResponse
import redis

r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
app = FastAPI()

channel_name = 'order_notifications'


@app.get("/new_order/{id}")
async def new_order(id: int):
    payload = {"order_id": id}
    json_string = json.dumps(payload, indent=4)
    r.publish(channel_name, json_string)
    return JSONResponse({'message': f'{json_string}'})

@app.get("/")
async def root():
    return JSONResponse({'message': 'Hello World'})