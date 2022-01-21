from apps.models import Model
from . import db

class NewLoan(Model):
    __table__ = 'neondataset'
    __primary_key__ = 'loanid'
    __timestamps__ = False

    def insert_loan(data = None):
        return db.table('loan').insert(data)

    def update_loan(id, data = None):
        return db.table('loan').where('loanid', '=', id).update(data)

    def delete_loan(id):
        return db.table('loan').where('loanid', '=', id).delete()