from fastapi import FastAPI
from app.Routers.Tron import RouterTron
import os,dotenv
dotenv.load_dotenv()
app = FastAPI(
    title='ApiCurrency',
    version='0.0.1',
    docs_url='/docs' if os.getenv('DOCS') == "True" else None,
    redoc_url='/redoc' if os.getenv('DOCS') == "True" else None,
)

app.include_router(RouterTron)