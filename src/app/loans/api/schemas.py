from marshmallow import fields
from app.ext import marsh

# class LoanSchema(marsh.Schema):
#     id = fields.Integer(dump_only=True)
#     loaned_object = fields.String()
#     student_name = fields.String()
#     student_id = fields.String()
#     auxiliar_name = fields.String()
#     auxiliar_id = fields.String()
#     loan_date = fields.DateTime()
#     loan_state = fields.String()

class LoanSchema(marsh.Schema):
    class Meta:
        fields = (
            'id',
            'loaned_object',
            'student_name',
            'student_id',
            'auxiliar_name',
            'auxiliar_id',
            'date',
            'state',
        )
