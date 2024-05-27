from fastapi import FastAPI
import uvicorn
import asyncio

app = FastAPI()


async def do_something():
    await asyncio.sleep(1.3)  # Non-blocking sleep
    return "Done"


@app.get("/")
async def read_root():
    await do_something()
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
