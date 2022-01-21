from apps.models import Model
from . import db

class Loan(Model):
    __table__ = 'neondataset2'
    __primary_key__ = 'idno'
    __timestamps__ = False

    def insert_data(data = None):
        return db.table('neondataset2').insert(data)

    def update_data(id, data = None):
        return db.table('neondataset2').where('idno', '=', id).update(data)

    def delete_data(id):
        return db.table('neondataset2').where('idno', '=', id).delete()
