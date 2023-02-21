from fastapi import FastAPI
from route import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



