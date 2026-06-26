
from fastapi import FastAPI
from app.routes.tutorials import router as tutorial_router
from app.routes.otp import router as otp_router
app=FastAPI(title="Hotel Management FastAPI")
app.include_router(tutorial_router,prefix="/api")
app.include_router(otp_router,prefix="/otp")
@app.get("/")
def root(): return {"status":"running"}
