from sqlite3 import Timestamp

from pydantic import BaseModel
from typing import Optional, List


class RequestLoan(BaseModel):
    cif: str = None


class LoanBase(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None

class CreateLoan(LoanBase):
    cif: str = None
    pass

class EditLoan(LoanBase):
    pass

class Loan(LoanBase):
    class Config:
        orm_mode = True

class ResponseLoan(BaseModel):
    loan_list: List[Loan]