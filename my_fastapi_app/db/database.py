from peewee import *

pg_db = PostgresqlDatabase('postgres', user='postgres', password='111',
                           host='localhost', port=5433)

class BaseModel(Model):
    class Meta:
        database = pg_db


class Application(BaseModel):
    id = AutoField(primary_key=True, column_name='id')
    file = TextField(column_name='file', default=None, null=True)
    isCar = BooleanField(column_name="isCar", default=None, null=True)
    status = IntegerField(column_name='status', default=0)
    result = TextField(column_name='result', default=None, null=True)

    class Meta:
        table_name = 'application'