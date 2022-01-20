from sqlite3 import Timestamp

from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None

class BorrowerData(BaseModel):
    idno: str = None

class CIF(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
    loan_status: int = None
    cif: str = None
    idno: int = None
    fname: str = None
    lname: str = None
    dob: Timestamp = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: Timestamp = None
    updatedate: Timestamp = None
    source: str = None



class ResponseCIF(BaseModel):
    cif_list: List[CIF]