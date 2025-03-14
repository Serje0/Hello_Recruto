from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_hello(name: str = None, message: str = None):
    return f"Hello {name}! {message}!"  