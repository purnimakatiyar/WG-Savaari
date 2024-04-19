from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.user_routes import router as user_router
from routes.ride_routes import router as rides_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(rides_router)
