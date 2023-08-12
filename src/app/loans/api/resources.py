from datetime import datetime
from flask import request, Blueprint
from flask_restful import Api, Resource

from app.common.error_handling import ObjectNotFound

from .schemas import LoanSchema
from ..models import Loan

loans_v1_0_blueprint = Blueprint('loans_v1_0_blueprint', __name__)
loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

api = Api(loans_v1_0_blueprint, catch_all_404s=True)

class LoanListResource(Resource):
    def get(self):
        loans = Loan.get_all()
        return loans_schema.dump(loans), 200

    def post(self):
        data = request.get_json(force=True)
        loan_dict = loan_schema.load(data)
        print(loan_dict['date'])
        new_loan = Loan(
            loaned_object = loan_dict['loaned_object'],
            student_name  = loan_dict['student_name'],
            student_id    = loan_dict['student_id'],
            auxiliar_name = loan_dict['auxiliar_name'],
            auxiliar_id   = loan_dict['auxiliar_id'],
            date          = datetime.strptime(loan_dict['date'],'%Y-%m-%d %H:%M:%S'),
            state         = loan_dict['state']
        )
        new_loan.save()
        # print("Estoy aquí", str(datetime.now()), new_loan)
        resp = loans_schema.dump([new_loan])
        return resp, 201
        # return {}, 201

class LoanResource(Resource):
    def get(self, loan_id):
        loan = Loan.get_by_id(loan_id)
        if loan is None: raise ObjectNotFound('Loan does not exist')
        return loan_schema.dump(loan), 200

    def put(self, loan_id):
        loan = Loan.get_by_id(loan_id)
        data = request.get_json(force=True)
        print(data, type(loan))
        if 'loaned_object' in data: loan.loaned_object = data['loaned_object']
        if 'student_name' in data: loan.student_name = data['student_name']
        if 'student_id' in data: loan.student_id = data['student_id']
        if 'auxiliar_name' in data: loan.auxiliar_name = data['auxiliar_name']
        if 'auxiliar_id' in data: loan.auxiliar_id = data['auxiliar_id']
        if 'date' in data: loan.date = datetime.strptime(data['date'],'%Y-%m-%d %H:%M:%S'),
        if 'state' in data: loan.date = data['state']
        loan.update()
        return loan_schema.dump(loan), 200

    def delete(self, loan_id):
        loan = Loan.get_by_id(loan_id)
        if not loan:
            return {
                'message': 'Loan does not exist'
            }, 400
        loan.delete()
        return {
            'message': 'Loan deleted successfully'
        }, 200


class AuxiliarResource(Resource):
    def get(self, auxiliar_id):
        print(auxiliar_id)
        loans = Loan.simple_filter(auxiliar_id = auxiliar_id)
        return loans_schema.dump(loans), 200

class StudentResource(Resource):
    def get(self, student_id):
        print(student_id)
        loans = Loan.simple_filter(student_id = student_id)
        return loans_schema.dump(loans), 200

class PendingResource(Resource):
    def get(self):
        loans = Loan.simple_filter(state = 'pending')
        return loans_schema.dump(loans), 200


api.add_resource(LoanListResource, '/api/v1.0/loans/')
api.add_resource(LoanResource, '/api/v1.0/loans/<int:loan_id>')
api.add_resource(PendingResource, '/api/v1.0/loans/pending')
api.add_resource(StudentResource, '/api/v1.0/student/<student_id>/')
api.add_resource(AuxiliarResource, '/api/v1.0/auxiliar/<auxiliar_id>/')
