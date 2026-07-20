from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menuitems"
)


@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)
