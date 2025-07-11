from fastapi import FastAPI
import requests
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)


@app.get("/proxy")
def proxy_request():
    logging.info("API1: Received request from user.")
    try:
        response = requests.get("http://api2:6066/hello")
        logging.info("API1: Forwarded request to API2.")
        return {"api1": "Success", "api2_response": response.json()}
    except Exception as e:
        logging.error(f"API1 Error: {e}")
        return {"error": str(e)}
