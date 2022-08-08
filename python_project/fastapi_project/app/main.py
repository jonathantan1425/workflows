from fastapi import FastAPI

from app.v1 import user

app = FastAPI(title="Sample API", openapi_url="/openapi.json")

app.include_router(user.router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8081, log_level="debug")
