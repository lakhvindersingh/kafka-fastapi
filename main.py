from fastapi import FastAPI
from api.routes import router
from settings import settings

def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)

    app.include_router(router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)