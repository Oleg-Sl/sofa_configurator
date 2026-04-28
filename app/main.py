import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import router as bitrix_router
# from app.core.config import settings
# from app.api.routers.routers import all_routers
# from app.services.scheduler_service import SchedulerService
# from app.api.dependencies import get_session_factory
# from app.jobs.run_task import run_tasks
# from app.jobs.run_dialog_tasks import run_dialog_tasks


sys.dont_write_bytecode = True


app = FastAPI(
    title='Sofa Configurator API',
    version="0.1.0",
    debug=True,
    root_path="/sofa-configurator",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# for router in all_routers:
app.include_router(bitrix_router)


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/test")
async def test():
    return {"test": 111, 'project_name': 'Sofa Configurator API'}


# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
# uvicorn main:app --reload
