import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database import Base, SessionLocal, engine
from app.routers import router
from app.services.seed import seed_portfolio_data

app = FastAPI(title='A. Sheik Farith Portfolio API', version='1.0.0')

origins = [origin.strip() for origin in os.getenv('CORS_ORIGINS', 'http://localhost:5173').split(',') if origin.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['GET', 'POST'], allow_headers=['*'])
app.include_router(router)


@app.on_event('startup')
def start_application() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_portfolio_data(db)


@app.get('/health', tags=['health'])
def health_check():
    return {'status': 'ok'}


# The Docker image copies the Vite build here so Railway can serve the site
# and API from a single public domain. Local Vite development is unchanged.
static_dir = Path(__file__).resolve().parents[1] / 'static'
if static_dir.is_dir():
    app.mount('/', StaticFiles(directory=static_dir, html=True), name='frontend')
