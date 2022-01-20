from apps.models import Model
from apps.models.NewLoanModel import NewLoan
from orator.orm import has_many

class Borrower(Model):
    __table__ = 'borrower'
    __primary_key__ = 'cif'

    @has_many('cif')
    def loan(self):
        return NewLoan

