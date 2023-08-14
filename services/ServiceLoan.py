from datetime import date
from typing import List
from config.connection import engine
from models.Loans import loans as loansTable
from schemas.Loan import Loan

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class ServiceLoan:
    def __init__(self):
        pass
    def create_loan(self, loan: Loan):
        loan.date = date.today()
        loan.status = "Prestado"
        loan_dict = loan.dict()
        try:
            session = sessionmaker(bind=engine)()
            ins = loansTable.insert().values(loan_dict)
            result = session.execute(ins)
            session.commit()
            session.close()
        except SQLAlchemyError as e:
            print("Error al guardar el elemento:", e)
            return False
        loan.id = result.inserted_primary_key[0]
        return loan

    def get_loans(self):
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).all()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener los elementos:", e)
            return False
        return [Loan(**loan._asdict()) for loan in result]
    
    def get_loan(self, loan_id: int):
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).filter_by(id=loan_id).first()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener el elemento:", e)
            return False
        return result
    def get_loan_by_student(self, student_document: int):
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).filter_by(student_document=student_document).all()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener el elemento:", e)
            return False
        return [Loan(**loan._asdict()) for loan in result]
    
    def return_loan(self,loan_id:int):
        try:
            session = sessionmaker(bind=engine)()
            upd = loansTable.update().where(loansTable.c.id == loan_id).values(status="Devuelto")
            session.execute(upd)
            session.commit()
            session.close()
        except SQLAlchemyError as e:
            print("Error al actualizar el elemento:", e)
            return False
        return self.get_loan(loan_id)
    
    def get_loans_by_day(self, day: str):
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).filter_by(date=day).all()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener el elemento:", e)
            return False
        return [Loan(**loan._asdict()) for loan in result]
    
    def get_pending_loans(self):
        print("El elemento")
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).filter_by(status="Prestado").all()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener los elementos:", e)
            return False
        return [Loan(**loan._asdict()) for loan in result]
    
    def get_loans_by_admin(self, admin_document: int):
        try:
            session = sessionmaker(bind=engine)()
            result = session.query(loansTable).filter_by(admin_document=admin_document).all()
            session.close()
        except SQLAlchemyError as e:
            print("Error al obtener los elementos:", e)
            return False
        return [Loan(**loan._asdict()) for loan in result]


