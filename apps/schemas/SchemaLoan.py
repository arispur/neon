from sqlite3 import Timestamp

from pydantic import BaseModel
from typing import Optional, List


class RequestLoan(BaseModel):
    loanid: str = None


class LoanBase(BaseModel):
    loan_type: int = None
    loan_status: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
    cif: str = None

class CreateLoan(LoanBase):
    loanid: str = None
    pass

class EditLoan(LoanBase):
    pass

class Loan(LoanBase):
    class Config:
        orm_mode = True

class ResponseLoan(BaseModel):
    loan_list: List[Loan]