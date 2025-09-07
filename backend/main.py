# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from backend.routes.upload import router as upload_router
# from backend.routes.gemini_analyze import router as gemini_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Relative imports (no 'backend.' prefix)
from routes.upload import router as upload_router
from routes.gemini_analyze import router as gemini_router


app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload_router)
app.include_router(gemini_router) 

