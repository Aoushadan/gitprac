import urllib
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-9DICSKS;"
    "DATABASE=LA;"
    "Trusted_Connection=yes;"
)
params = urllib.parse.quote_plus(conn_str)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

try:
    with engine.connect():
        print("Connection successful.")
except Exception as e:
    print(f"Connection failed: {e}")

metadata = MetaData()

employee_table = Table(
    'employee',
    metadata,
    Column('emp id', Integer, key='emp_id', primary_key=True, nullable=False),
    Column('name', String(100), nullable=False),
    Column('salary', Integer, nullable=False),
)

try:
    metadata.create_all(engine)
    print("Table employee created successfully.")
except Exception as e:
    print(f"Failed to create table: {e}")

engine.dispose()
