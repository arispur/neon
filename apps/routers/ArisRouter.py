import json
from fastapi import APIRouter, Body, Response
from apps.controllers.ArisController.ArisController import ControllerAris as aris
router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "687735",
}, indent=2)

example_input_loan = json.dumps({
    "loanid": 3000,
    "loan_type": 1,
    "loan_status": 1,
    "loan_amount": 3000000,
    "loan_tenure": 24,
    "interest": 15,
    "cif": "4000"
}, indent=2)

example_edit_loan = json.dumps({
    "loan_type": 2,
    "loan_status": 2,
    "loan_amount": 4000000,
    "loan_tenure": 6,
    "interest": 15,
    "cif": "5000"
}, indent=2)

@router.post("/get_loan_by_cif")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = aris.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = aris.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/index_loan")
async def index_loan(response: Response):
    result = aris.index_loan()
    response.status_code = result.status
    return result

@router.post("/loan")
async def store_loan(response: Response, input_data=Body(..., example=example_input_loan)):
    result = aris.store_loan(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/loan/{id}")
async def show_loan(response: Response, id: int):
    result = aris.show_loan(id)
    response.status_code = result.status
    return result

@router.put("/loan/{id}")
async def show_loan(response: Response, id: int, input_data=Body(..., example=example_edit_loan)):
    result = aris.edit_loan(id, input_data=input_data)
    response.status_code = result.status
    return result

@router.delete("/loan/{id}")
async def delete_loan(response: Response, id: int):
    result = aris.delete_loan(id)
    response.status_code = result.status
    return result

@router.get("/loan_by_borrower/{id}")
async def show_borrower(response: Response, id: int):
    result = aris.show_loan_in_borrower(id)
    response.status_code = result.status
    return result