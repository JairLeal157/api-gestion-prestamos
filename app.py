from fastapi import FastAPI
import api.LoanRoute as LoanRoute

app = FastAPI()

app.include_router(LoanRoute.router)
@app.get("/")
def read_root():
    return "App is running"
