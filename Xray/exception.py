# Import necessary modules: os and sys
import os
import sys

# Define a function to get detailed error message
def error_message_detail(error: Exception, error_detail: sys) -> str:
   _, _, exc_tb = error_detail.exc_info() # Get detailed error information

   file_name: str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] # Get the name of the file where the error occurred

   error_message: str = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format( # Create the detailed error message
       file_name, exc_tb.tb_lineno, str(error)
   )

   return error_message # Return the detailed error message

# Define a custom exception class XRayException
class XRayException(Exception):
   def __init__(self, error_message, error_detail):
       """
       Initialize the custom exception class with error message and detailed error information
       """
       super().__init__(error_message) # Call the constructor of the base class Exception

       self.error_message: str = error_message_detail( # Initialize error_message with detailed error message
           error_message, error_detail=error_detail
       )

   def __str__(self):
       return self.error_message # Return the detailed error message when the object is converted to a string