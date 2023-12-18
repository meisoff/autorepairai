from peewee import *
from os import environ


pg_db = PostgresqlDatabase(user=environ["POSTGRES_USER"], password=environ["POSTGRES_PASSWORD"],
                           host=environ["HOSTNAME"], database=environ["POSTGRES_DB"], port=5432)

# pg_db = PostgresqlDatabase('postgres', user='postgres', password='postgres',
#                            host='postgres', port=5432)

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
    mark = TextField(column_name='mark', default=None, null=True)
    model = TextField(column_name='model', default=None, null=True)
    year = TextField(column_name='year', default=None, null=True)
    status = IntegerField(column_name='status', default=0)
    result = TextField(column_name='result', default=None, null=True)
    prices = TextField(column_name='prices', default=None, null=True)
    account_id = IntegerField(column_name='account_id', default=0, null=False)

    class Meta:
        table_name = 'application'