from db_details import user, pwd, db, host
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

try:
    conn = engine.connect()
    print("Successfull connection")
    conn.close()
except Exception as e:
    print("Could not connect to the database: ", e)



