from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import List, Union
from Code.main_function import *
import uvicorn
import torch

app = FastAPI()

class Item(BaseModel):
    url: str


async def process_item(item: Item):
    try:
        result = await mainDet(item.url)
        result = json.loads(result) #parses into object
        return result
    finally:
        torch.cuda.empty_cache()
        pass


@app.get("/status")
async def status():
    return "AI Server in running"

@app.post("/face")
async def create_items(items: Item):
    try:
        results = await process_item(items)
        return results
    except Exception as e:
        return {"AI": f"Error: {str(e)}"}

# pip install -r requirements.txt
# python -m uvicorn Code.main:app --reload
# pip install -upgrade ultralytics
