
from sqlalchemy import Column,Integer,String,Boolean,JSON
from app.database import Base
class Tutorial(Base):
 __tablename__="tutorials"
 id=Column(Integer,primary_key=True)
 title=Column(String(255))
 description=Column(String(500))
 published=Column(Boolean,default=False)
class User(Base):
 __tablename__="user"
 id=Column(Integer,primary_key=True)
 phone=Column(String(30))
 email=Column(String(255),unique=True)
 password=Column(String(255))
 roles=Column(JSON)
class UserOtp(Base):
 __tablename__="user_otp"
 id=Column(Integer,primary_key=True)
 otp=Column(String(10))
 phone_number=Column(String(30))
 email=Column(String(255))
