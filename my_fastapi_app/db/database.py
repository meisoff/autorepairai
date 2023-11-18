from peewee import *

pg_db = PostgresqlDatabase('postgres', user='postgres', password='111',
                           host='localhost', port=5433)

class BaseModel(Model):
    class Meta:
        database = pg_db


class Account(BaseModel):
    id = AutoField(primary_key=True, column_name='id')
    login = TextField(column_name='login', null=False)
    password = TextField(column_name='password', null=False)
    userGuid = TextField(column_name='userGuid', unique=True, null=False)

    class Meta:
        table_name = 'account'

class Application(BaseModel):
    id = AutoField(primary_key=True, column_name='id')
    file = TextField(column_name='file', default=None, null=True)
    isCar = BooleanField(column_name="isCar", default=None, null=True)
    model = TextField(column_name='model', default=None, null=True)
    status = IntegerField(column_name='status', default=0)
    result = TextField(column_name='result', default=None, null=True)
    prices = TextField(column_name='prices', default=None, null=True)
    account_id = IntegerField(column_name='account_id', default=0, null=False)

    class Meta:
        table_name = 'application'