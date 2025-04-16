import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #in which line, file the exception has occured
    file_name=exc_tb.tb_frame.f_code.co_filename #custome exception handling
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

# when error is found, run error_message_detail
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # to print
    def __str__(self):
        return self.error_message


# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)

