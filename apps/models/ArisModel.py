from apps.models import Model


class Aris(Model):
    __table__ = 'neondataset'
    __primary_key__ = 'loanid'
