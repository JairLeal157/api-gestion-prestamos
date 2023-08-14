from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.connection import meta, engine

loans = Table(
    "loans", meta, 
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("student_name", String(50), nullable=False),
    Column("student_document", Integer, nullable=False),
    Column("admin_name", String(50), nullable=False),
    Column("admin_document", Integer, nullable=False),
    Column("date", Date, nullable=False),
    Column("item", String(50), nullable=False),
    Column("status", String(50), nullable=False)
)

meta.create_all(engine)
