import sys

class CustomException(Exception):
    def __init__(self, error, error_details: sys = None):
        super().__init__(error)

        self.error_message = str(error)

        if error_details is not None:
            _, _, exc_tb = error_details.exc_info()

            if exc_tb is not None:
                self.line_no = exc_tb.tb_lineno
                self.file_name = exc_tb.tb_frame.f_code.co_filename
            else:
                self.line_no = None
                self.file_name = None
        else:
            self.line_no = None
            self.file_name = None

    def __str__(self):
        if self.file_name and self.line_no:
            return (
                f"Error in [{self.file_name}] at line [{self.line_no}]: "
                f"{self.error_message}"
            )
        else:
            return f"Error: {self.error_message}"