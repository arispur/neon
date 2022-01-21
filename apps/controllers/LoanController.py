from optparse import Values
from unicodedata import name
from numpy import where
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import CIF, BorrowerData, RequestCIF, ResponseCIF
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
from apps.models import db

SALT = PARAMS.SALT.salt


class ControllerLoan(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
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
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
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
    def delete_acc_by_ktp(cls, id: int):
        result = BaseResponse()
        result.status = 400
        try:
            if Loan.delete_data(id):
                result.status = 200
                result.message = "Berhasil menghapus data: " + str(id)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        return result

    @classmethod
    def show_data(cls, id: int):
        result = BaseResponse()
        result.status = 400
        try:
            if id is not None:
                data = Loan.where('idno', '=', id).get().serialize()
                if not data:
                    e = "id not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
                else:
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseCIF(**{"cif_list": data})
                    Log.info(result.message)
            else:
                e = "id not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        return result
        
    @classmethod
    def edit_data(cls, id: int, input_data=None):
        input_loan = CIF(**input_data)
        result = BaseResponse()
        result.status = 400
        try:
            with db.transaction():
                if Loan.update_data(id, input_loan):
                    result.status = 200
                    result.message = "Berhasil Mengubah Data: " + str(id)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)
        return result

    @classmethod
    def store_data(cls, input_data=None):
        input_loan = CIF(**input_data)
        result = BaseResponse()
        result.status = 400
        try:
            with db.transaction():
                if Loan.insert_data(input_loan):
                    result.status = 200
                    result.message = "Sukses menyimpan data"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result




