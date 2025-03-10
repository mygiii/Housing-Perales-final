from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import db_model, schemas
from app.connect_to_db import SessionLocal, engine
from fastapi import FastAPI

app = FastAPI()
router = APIRouter()

# Créer la table si non existante (pour développement)
db_model.Base.metadata.create_all(bind=engine)

def get_db():
    # Ouvre une session de base de données
    db = SessionLocal()
    try:
        yield db
    finally:
        # Ferme la session de base de données
        db.close()

@router.get("/houses", response_model=list[schemas.House])
def get_houses(db: Session = Depends(get_db)):
    # Récupère toutes les maisons de la base de données
    houses = db.query(db_model.House).all()
    return houses

@router.post("/houses", response_model=schemas.House)
def create_house(house: schemas.HouseCreate, db: Session = Depends(get_db)):
    # Crée une nouvelle maison dans la base de données
    db_house = db_model.House(**house.dict())
    db.add(db_house)
    db.commit()
    # Rafraîchit l'objet db_house pour obtenir les données mises à jour
    db.refresh(db_house)
    return db_house

app.include_router(router)