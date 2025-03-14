from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}&{massage}")
def get_hello(name: str = None, massage: str = None):
    return "Hello " + name + "! " + massage + "!"   