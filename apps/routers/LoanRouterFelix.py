import json
from urllib import response
from fastapi import APIRouter, Body, Response
from apps.controllers.FelixController import ControllerFelix as loan

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "864921",
}, indent=2)

example_update = json.dumps({
    "loanid" :   1,
    "loan_type" :   3,
    "loan_status": 1,
    "loan_amount" : 61044325,
    "loan_tenure" :   9,
    "interest" :   15,
    "idno" :   36880286492110004,
    "fname" :   "Valeria",
    "lname" :   "Nelson",
    "dob" :   "1988-4-27 00:00:00",
    "gender" :   "Female",
    "marital_status" :   "Married",
    "income" :   16692000,
    "phone" :   "110-4812-00",
    "email" :   "v.nelson@ymail.com",
    "isphoneverified" :   "0",
    "isemailverified" :   "1",
    "createdate" :   "2021-3-4 00:00:00",
    "updatedate" :   "2021-3-12 00:00:00",
    "source" :   "Web On Boarding",
}, indent=2)


example_input = json.dumps({
    "loanid" :   1,
    "loan_type" :   3,
    "loan_status": 1,
    "loan_amount" : 61044325,
    "loan_tenure" :   9,
    "interest" :   15,
    "cif" : 10,
    "idno" :   36880286492110004,
    "fname" :   "Valeria",
    "lname" :   "Nelson",
    "dob" :   "1988-4-27 00:00:00",
    "gender" :   "Female",
    "marital_status" :   "Married",
    "income" :   16692000,
    "phone" :   "110-4812-00",
    "email" :   "v.nelson@ymail.com",
    "isphoneverified" :   "0",
    "isemailverified" :   "1",
    "createdate" :   "2021-3-4 00:00:00",
    "updatedate" :   "2021-3-12 00:00:00",
    "source" :   "Web On Boarding",
}, indent=2)

@router.post("/get_loan_by_cif_Felix")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug_Felix")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result


###################################################################################

@router.get("/get_felix/{cif}")
async def get_felix(response: Response,cif: str):
    result = loan.get_felix(cif)
    response.status_code = result.status
    return result

@router.put("/cif/{cif}")
async def edit_data(response: Response, cif: int, input_data=Body(..., example=example_update)):
    result = loan.edit_data(cif, input_data=input_data)
    response.status_code = result.status
    return result


@router.delete("/deletedata/{cif}")
async def delete_data(response: Response, cif: int):
    result = loan.delete_data(cif)
    response.status_code = result.status
    return result

@router.post("/post")
async def postdata(response: Response, input_data=Body(..., example=example_input)):
    result = loan.postdata(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/get_borrower/{cif}")
async def get_borrower(response: Response, cif: str):
    result = loan.get_borrower(cif)
    response.status_code = result.status
    return result