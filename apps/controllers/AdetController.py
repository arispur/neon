from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF
from apps.schemas.SchemaLoan1 import RequestLoan, ResponseLoan, CreateLoan, EditLoan
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.NewLoanModel1 import NewLoan
from apps.models.AdetModel import Adet

SALT = PARAMS.SALT.salt


class ControllerAdet(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Adet.where('cif', '=', input_data.cif).get().serialize()
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
                data = Adet.where('cif', '=', input_data.cif).get().serialize()
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
    def show_cif(cls, id: int):
        result = BaseResponse()
        result.status = 400

        try:
            if id is not None:
                data = Adet.where('cif', '=', id).get().serialize()
                if not data:
                    e = "cif data not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseCIF(**{"cif_list": data})
                    Log.info(result.message)
            else:
                e = "cif data not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def edit_cif(cls, cif: str, input_data=None):
        input_loan = EditLoan(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            loan = NewLoan.find(cif)

            loan.loan_type = input_loan.loan_type,
            loan.loan_status = input_loan.loan_status,
            loan.loan_amount = input_loan.loan_amount,
            loan.loan_tenure = input_loan.loan_tenure,
            loan.interest = input_loan.interest,
            loan.loanid = input_loan.loanid

            loan.save()

            # NewLoan.store_loans(input_loan)

            result.status = 200
            result.message = "Success"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_cif(cls, cif: int):
        result = BaseResponse()
        result.status = 400

        try:
            if id is not None:
                loan = NewLoan.find(cif)
                loan.delete()
                result.status = 200
                result.message = "Success"

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