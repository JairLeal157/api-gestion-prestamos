# import sys, os
# parent_dir = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(parent_dir)
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# class BaseModelMixin:
#     pass
from app.db import db, BaseModelMixin
from datetime import datetime

class Loan(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    loaned_object = db.Column(db.String)
    student_name = db.Column(db.String)
    student_id = db.Column(db.String)
    auxiliar_name = db.Column(db.String)
    auxiliar_id = db.Column(db.String)
    loan_date = db.Column(db.DateTime)
    loan_state = db.Column(db.String)

    def __init__(self, loaned_object, student_name, student_id, auxiliar_name, auxiliar_id, loan_date = datetime.now, loan_state = "pending") -> None:
        self.loaned_object = loaned_object
        self.student_name = student_name
        self.student_id = student_id
        self.auxiliar_name = auxiliar_name
        self.auxiliar_id = auxiliar_id
        self.loan_date = loan_date
        self.loan_state = loan_state

    def __repr__(self):
        return f"Loan({self.loaned_object}, {self.loan_state})"

    def __str__(self):
        return f"{self.loaned_object}, {self.loan_state}"
