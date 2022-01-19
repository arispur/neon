import json
from fastapi import APIRouter, Body, Response
from apps.controllers.ArisController import ControllerAris as aris

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

@router.post("/get_loan_by_cif_created_by_aris")
async def get_loan_by_cif_created_by_aris(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = aris.get_loan_by_cif_created_by_aris(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug_created_by_aris")
async def get_loan_by_cif_debug_created_by_aris(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = aris.get_loan_by_cif_debug_created_by_aris(input_data=input_data)
    response.status_code = result.status
    return result