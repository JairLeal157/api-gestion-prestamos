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
        return loans_schema.dump(loans)

    def post(self):
        data = request.get_json()
        loan_dict = loan_schema.load(data)
        new_loan = Loan(
            loaned_object = loan_dict['loaned_object'],
            student_name  = loan_dict['student_name'],
            student_id    = loan_dict['student_id'],
            auxiliar_name = loan_dict['auxiliar_name'],
            auxiliar_id   = loan_dict['auxiliar_id'],
            loan_date     = loan_dict['loan_date'],
            loan_state    = loan_dict['state']
        )
        new_loan.save()
        resp = loans_schema.dump(new_loan)
        return resp, 201

class LoanResource(Resource):
    def get(self, loan_id):
        loan = Loan.get_by_id(loan_id)
        if loan is None: raise ObjectNotFound('Loan does not exist')
        return loan_schema.dump(loan)



api.add_resource(LoanListResource, '/api/v1.0/loans/')
api.add_resource(LoanResource, '/api/v1.0/loans/<int:loan_id>')
