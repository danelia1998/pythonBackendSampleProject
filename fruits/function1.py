from app import app


@app.get("/fruits/function1")
def books_f1():
    return {"message": "fruits function 1"}
