from apps.models import Model


class Adet(Model):
    __table__ = 'neondataset'
    __primary_key__ = 'loanid'
