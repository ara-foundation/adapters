from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/twitter/callback")
async def twitter_callback():
    return {"message": "it's twitter callback page"}