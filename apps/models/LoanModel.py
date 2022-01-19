from apps.models import Model


class Loan(Model):
    __table__ = 'neondataset'
    __primary_key__ = 'loanid'
