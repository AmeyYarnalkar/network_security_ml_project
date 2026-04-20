import sys
class CustomException(Exception):
    def __init__(self,error,error_details:sys):
        super().__init__(error) # executed not to break the usual work flow 
        
        _,_,exc_tb = error_details.exc_info()
        
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        message = f"Error occurred in script [{self.file_name}] at line [{self.line_no}]: {str(self.args[0])}"
        return message
    
    