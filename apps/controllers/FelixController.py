from os import remove
from urllib import request
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import CIF, RequestCIF, ResponseBOR, ResponseCIF
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import LoanFelix
from apps.models.BorrowerModelFelix import Borrower
SALT = PARAMS.SALT.salt


class ControllerFelix(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = LoanFelix.where('cif', '=', input_data.cif).get().serialize()
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
                data = LoanFelix.where('cif', '=', input_data.cif).get().serialize()
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


# ### 
    @classmethod
    def get_felix(cls, cif: str):
        result = BaseResponse()
        result.status = 400

        try:
            if  cif is not None:
                data = LoanFelix.where('cif', '=', cif).get().serialize()
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
    def edit_data(cls, cif: str,input_data=None):
        input_data = CIF(**input_data)
        result = BaseResponse()
        result.status = 400
        try:
            loan = Loan.find(cif)
            loan.loanid  = input_data.loanid,
            loan.loan_type  = input_data.loan_type,
            loan.loan_amount  = input_data.loan_amount,
            loan.loan_tenure  = input_data.loan_tenure,
            loan.interest  = input_data.interest,
            loan.idno  = input_data.idno,
            loan.fname  = input_data.fname,
            loan.lname  = input_data.lname,
            loan.dob  = input_data.dob,
            loan.gender  = input_data.gender,
            loan.marital_status  = input_data.marital_status,
            loan.income  = input_data.income,
            loan.phone  = input_data.phone,
            loan.email  = input_data.email,
            loan.isphoneverified  = input_data.isphoneverified,
            loan.isemailverified  = input_data.isemailverified,
            loan.createdate  = input_data.createdate,
            loan.updatedate  = input_data.updatedate,
            loan.source  = input_data.source

            loan.save()
            result.status = 200
            result.message = "updated"
        except Exception as e:

            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result


    @classmethod
    def postdata(cls,input_data=None):
        input_data = CIF(**input_data)
        result = BaseResponse()
        result.status = 400
        try:
            loan = Loan()
            loan.loanid  = input_data.loanid,
            loan.loan_type  = input_data.loan_type,
            loan.loan_amount  = input_data.loan_amount,
            loan.loan_tenure  = input_data.loan_tenure,
            loan.interest  = input_data.interest,
            loan.cif = input_data.cif,
            loan.idno  = input_data.idno,
            loan.fname  = input_data.fname,
            loan.lname  = input_data.lname,
            loan.dob  = input_data.dob,
            loan.gender  = input_data.gender,
            loan.marital_status  = input_data.marital_status,
            loan.income  = input_data.income,
            loan.phone  = input_data.phone,
            loan.email  = input_data.email,
            loan.isphoneverified  = input_data.isphoneverified,
            loan.isemailverified  = input_data.isemailverified,
            loan.createdate  = input_data.createdate,
            loan.updatedate  = input_data.updatedate,
            loan.source  = input_data.source

            loan.save()
            result.status = 200
            result.message = "inputed"
        except Exception as e:

            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_data(cls, cif: int):
        result = BaseResponse()
        result.status = 400
        try:
            if cif is not None:
#               data = Loan.where('cif', '=', input_data.cif).get().serialize()
                data = LoanFelix.find(cif)
                data.delete()
                result.status = 200
                result.message = "Deleted"
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
    def get_borrower(cls, cif: int):
        result = BaseResponse()
        result.status = 400

        try:
            if cif is not None:
                data = Borrower.find(cif).loan.serialize()
                if not data:
                    e = "loan not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseBOR(**{"bor_list": data})
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