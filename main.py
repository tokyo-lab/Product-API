from fastapi import FastAPI

app = FastAPI()

# create route
@app.get("/")
def root():
    return {"Hello": "Worldx"}