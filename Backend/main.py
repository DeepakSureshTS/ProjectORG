from fastapi import FastAPI
from route import user

app = FastAPI()
app.include_router(user)



