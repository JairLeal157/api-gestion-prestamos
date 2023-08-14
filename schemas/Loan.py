from datetime import date as Date
from pydantic import BaseModel


class Loan(BaseModel):
    id: int | None = None
    student_name: str
    student_document: int
    admin_name: str
    admin_document: int
    date:  Date | None = None
    item: str
    status: str | None = None

    class Config:
        orm_mode = True


example_loan = {
    "post": Loan(
        student_name="Juan",
        student_document=123456789,
        admin_name="Pedro",
        admin_document=987654321,
        item="Libro",
    ),
    "get": Loan(
        id=1,
        student_name="Juan",
        student_document=123456789,
        admin_name="Pedro",
        admin_document=987654321,
        date="2021-10-10",
        item="Libro",
        status="Prestado"
    )
}
