from fastapi import FastAPI


app = FastAPI()

EMPLOYEES = [
    {"firstname": "Dawid", "lastname": "Jakieła"},
    {"firstname": "Jan", "lastname": "Kowalski"},]

@app.get('/')
async def index_api():
    return {"message": "The example of single use of FastAPI!"}

@app.get("/employees")
async def get_employees():
    return EMPLOYEES

@app.get('/employees/{name}')
async def get_employee(name: str):
    for emp in EMPLOYEES:
        if emp['firstname'] == name:
            return emp
    return {'employee': "Employee with lastname {name} was not found"}, 404
    