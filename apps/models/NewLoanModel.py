from apps.models import Model
# from apps.models.Borrower import Borrower
# from orator.orm import belongs_to
from . import db

class NewLoan(Model):
    __table__ = 'neondataset'
    __primary_key__ = 'loanid'

    # @belongs_to
    # def borrower(self):
    #     return Borrower

    # def get_loans(db: Session, skip: int = 0, limit: int = 100):
    #     return db.query(models.Loan).offset(skip).limit(limit).all()