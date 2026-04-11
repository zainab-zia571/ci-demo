from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Calculator API is running'}


@app.get('/add')
def add(a: float, b: float):
    return {'operation': 'add', 'a': a, 'b': b, 'result': a + b}


@app.get('/subtract')
def subtract(a: float, b: float):
    return {'operation': 'subtract', 'a': a, 'b': b, 'result': a - b}


@app.get('/multiply')
def multiply(a: float, b: float):
    return {'operation': 'multiply', 'a': a, 'b': b, 'result': a * b}


@app.get('/divide')
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail='Cannot divide by zero')
    return {'operation': 'divide', 'a': a, 'b': b, 'result': a / b}


