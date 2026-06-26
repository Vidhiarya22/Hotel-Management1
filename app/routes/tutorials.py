
from fastapi import APIRouter
router=APIRouter()
@router.get("/tutorials")
def get_all(): return {"message":"Tutorial endpoints converted from Spring Boot"}
