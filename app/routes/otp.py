
from fastapi import APIRouter
import random
router=APIRouter()
@router.post("/send-otp")
def send_otp(phone:str):
 return {"phone":phone,"otp":str(random.randint(100000,999999))}
@router.post("/login")
def login():
 return {"accessToken":"replace-with-jwt"}
