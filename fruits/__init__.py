from app import app


@app.get("/fruits")
def get_books():
    # code to return some books
    return {"message": "fruits"}


from fruits.function1 import *
from fruits.function2 import *
