import uvicorn
from fastapi import *

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello world"}


from books import *
from fruits import *

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000)
