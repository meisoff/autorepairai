import database

# Скрипт для создания таблиц
database.pg_db.connect()
database.pg_db.create_tables([database.Account, database.Application])
