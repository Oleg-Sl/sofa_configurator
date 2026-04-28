import pathlib
import logging
from typing import Annotated
from fastapi import APIRouter, Request, Query, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas.credentials import CredentialsInputSchema, CredentialSchema


router = APIRouter(
    prefix="/bitrix",
    tags=["Bitrix"],
)


templates = Jinja2Templates(directory="app/static/templates")


pathlib.Path("logs").mkdir(parents=True, exist_ok=True)
logging.basicConfig(level=logging.INFO, filename="logs/bitrix.log",
                    format="%(asctime)s %(levelname)s %(message)s")



@router.get("/index", response_class=HTMLResponse)
async def index1(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")


@router.post("/index", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html")


@router.post("/install", response_class=HTMLResponse)
async def install(
    request: Request,
    DOMAIN: Annotated[str, Query()],
    APP_SID: Annotated[str, Query()],
    data: Annotated[CredentialsInputSchema, Form()],
) -> HTMLResponse:
    credential_data = CredentialSchema(
        domain=DOMAIN,
        application_token=APP_SID,
        **data.model_dump(),
    )
    return templates.TemplateResponse(
        request=request,
        name="install.html",
        context={
        }
    )
