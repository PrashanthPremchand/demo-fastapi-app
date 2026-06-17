from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "statue": "sucess",
        "message": "FastAPI is running flawlessly inside VS Code!"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {
        "item_id": item_id, 
        "searched_for": query_param
    }