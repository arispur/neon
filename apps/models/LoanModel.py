from apps.models import Model


class Loan(Model):
    __table__ = 'mytable4'
    __primary_key__ = 'loanid'
