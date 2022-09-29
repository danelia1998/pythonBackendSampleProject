from app import app


@app.get("/fruits/function2")
def books_f2():
    return {"message": "fruits function 2"}
