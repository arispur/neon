from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF
from apps.schemas.SchemaLoan import RequestLoan, ResponseLoan, CreateLoan, EditLoan
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.NewLoanModel import NewLoan
from apps.models.BorrowerModel import Borrower
from apps.models import db
SALT = PARAMS.SALT.salt

class ControllerAris(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = NewLoan.where('cif', '=', input_data.cif).get().serialize()
                if not data:
                    e = "cif not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else :
                    result.status = 200
                    result.message = "Success"
                    result.data = encoder_app(ResponseCIF(**{"cif_list": data}).json(), SALT)
                    Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_loan_by_cif_debug(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = NewLoan.where('cif', '=', input_data.cif).get().serialize()
                if not data:
                    e = "cif not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseCIF(**{"cif_list": data})
                    Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def index_loan(cls):
        result = BaseResponse()
        result.status = 400
        try:
            data = NewLoan.paginate(15, 2).serialize()
            result.status = 200
            result.message = "Success"
            result.data = ResponseLoan(**{"loan_list": data})
            Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def store_loan(cls, input_data=None):
        input_loan = CreateLoan(**input_data)
        result = BaseResponse()
        result.status = 400

        try:

            with db.transaction():
                if NewLoan.insert_loan(input_loan):
                    result.status = 200
                    result.message = "Success Input Loan"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def edit_loan(cls, id: int, input_data=None):
        input_loan = EditLoan(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            with db.transaction():
                if NewLoan.update_loan(id, input_loan):
                    result.status = 200
                    result.message = "Success Edit Loan ID: " + str(id)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def show_loan(cls, id: int):
        result = BaseResponse()
        result.status = 400

        try:
            if id is not None:
                data = NewLoan.where('loanid', '=', id).get().serialize()
                if not data:
                    e = "loan not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoan(**{"loan_list": data})
                    Log.info(result.message)
            else:
                e = "loan not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_loan(cls, id: int):
        result = BaseResponse()
        result.status = 400

        try:
            if NewLoan.delete_loan(id):
                result.status = 200
                result.message = "Success Delete Loan ID: " + str(id)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def show_loan_in_borrower(cls, id: int):
        result = BaseResponse()
        result.status = 400

        try:
            if id is not None:
                data = Borrower.find(id).loan.serialize()
                if not data:
                    e = "loan not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoan(**{"loan_list": data})
                    Log.info(result.message)
            else:
                e = "loan not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result