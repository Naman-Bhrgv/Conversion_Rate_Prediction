import sys

# generates custom error message
def error_detail(err,err_dt):

    _,_,exc_tb=err_dt.exec_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error encountered in program [{0}] at line [{1}] containing message [{2}].".format(file_name,exc_tb.tb_lineno,str(err))

    return error_message
class CustomException(Exception): #inherits from python exception class

    def __init__(self,error_message,error_detail):

        super().__init__(error_message)

        self.error_message= error_detail(error_message,error_detail)

    def __str__(self):

        return self.error_message
    




