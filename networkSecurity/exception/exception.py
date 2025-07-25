import sys
import traceback
from networkSecurity.logging.logger  import logger



class NetworkSecurityExcepion(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message
        _, _, exc_tb = error_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return "Error occurred in script name [{0}] at line number [{1}] with error message [{2}]".format(self.file_name,self.lineno, str(self.error_message))
        
if __name__ == "__main__":
    try:
        logger.info("Starting the exception handling demo")
        a = 1 / 0
    except Exception as e:
        logger.info("Exception has been raised")
        raise NetworkSecurityExcepion(e, sys) from e
    finally:
        logger.info("Finally block executed")