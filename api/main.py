from fastapi import FastAPI
from controllers import health_check_controller

app = FastAPI()

app.include_router(health_check_controller.router)