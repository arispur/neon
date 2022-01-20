import json
from fastapi import APIRouter, Body, Response
from apps.controllers.AdetController import ControllerAdet as adet

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

example_edit_cif = json.dumps({
    "loanid": 5000,
    "loan_type": 2,
    "loan_status": 2,
    "loan_amount": 4000000,
    "loan_tenure": 6,
    "interest": 15,
}, indent=2)

@router.post("/get_loan_by_cif")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = adet.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = adet.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/loan/{cif}")
async def show_cif(response: Response, cif: int):
    result = adet.show_cif(cif)
    response.status_code = result.status
    return result

@router.put("/loan/{cif}")
async def show_cif(response: Response, cif: str, input_data=Body(..., example=example_edit_cif)):
    result = adet.edit_cif(cif, input_data=input_data)
    response.status_code = result.status
    return result

@router.delete("/loan/{cif}")
async def delete_loan(response: Response, cif: int):
    result = adet.delete_cif(cif)
    response.status_code = result.status
    return result