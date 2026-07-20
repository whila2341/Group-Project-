from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import system_documentation as controller
from ..schemas import System_doc as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["System Documentation"],
    prefix="/system-documentation"
)


@router.post("/", response_model=schema.SystemDocumentationResponse)
def create(request: schema.SystemDocumentationCreate,
           db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.SystemDocumentationResponse])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.SystemDocumentationResponse)
def read_one(item_id: int,
             db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.SystemDocumentationResponse)
def update(item_id: int, request: schema.SystemDocumentationUpdate,
           db: Session = Depends(get_db)):
    return controller.update(
        db=db,
        request=request,
        item_id=item_id
    )


@router.delete("/{item_id}")
def delete(item_id: int,
           db: Session = Depends(get_db)):
    return controller.delete(
        db=db,
        item_id=item_id
    )