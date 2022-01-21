from apps.models import Model
from apps.models.LoanModel import Loan, LoanFelix
from orator.orm import has_many


class Borrower(Model):
    __table__ = 'borrower'
    __primary_key__ = 'cif'

    @has_many("cif")
    def loan(self):
        return LoanFelix