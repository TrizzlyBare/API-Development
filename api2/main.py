from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


@app.get("/hello")
def say_hello():
    logging.info("API2: Received request from API1.")
    return {"message": "Hello from API2 on port 6066!"}
