from fastapi import FastAPI

from api.routes import election, ping


def create_application() -> FastAPI:
    application = FastAPI(
        title="Elections API",
        description="Api interface for elections scraper data",
        version="v0.0.1",
        contact={
            "name": "Nduati Daniel Chege",
            "url": "https://danielchege.me",
        },
        docs_url="/",
        redoc_url="/docs",
    )
    application.include_router(ping.router)
    application.include_router(election.router)
    return application


app = create_application()
