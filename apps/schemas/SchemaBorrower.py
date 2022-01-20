from sqlite3 import Timestamp

from pydantic import BaseModel
from typing import Optional, List


class RequestLoan(BaseModel):
    loanid: str = None


class Loan(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
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


class ResponseLoan(BaseModel):
    loan_list: List[Loan]