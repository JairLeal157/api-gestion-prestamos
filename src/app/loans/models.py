from app.db import db, BaseModelMixin
from datetime import datetime

class Loan(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    loaned_object = db.Column(db.String)
    student_name = db.Column(db.String)
    student_id = db.Column(db.String)
    auxiliar_name = db.Column(db.String)
    auxiliar_id = db.Column(db.String)
    date = db.Column(db.DateTime)
    state = db.Column(db.String)

    def __init__(self,
                 loaned_object: int,
                 student_name: str,
                 student_id: str,
                 auxiliar_name: str,
                 auxiliar_id: str,
                 date: datetime = datetime.now().replace(microsecond=0),
                 state: str = "pending") -> None:
        self.loaned_object = loaned_object
        self.student_name = student_name
        self.student_id = student_id
        self.auxiliar_name = auxiliar_name
        self.auxiliar_id = auxiliar_id
        self.date = date
        self.state = state

    def __repr__(self):
        return f"Loan({self.loaned_object}, {self.state})"

    def __str__(self):
        return f"{self.loaned_object}, {self.state}"
