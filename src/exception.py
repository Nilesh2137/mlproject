import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error message including script name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Fix typo in attribute

    error_message = "Error occurred in python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # Intentional error (divide by zero)
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)
