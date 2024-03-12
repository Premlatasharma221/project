import sys
import logging 


def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    ## this will give us all the info like in which line exception occured
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg ="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
       file_name,exc_tb.tb_lineno,str(error))
    return error_msg


       
        #exc_tb=trackback of time of the exception
        #tb_frame=trackback of local_var,global_var 
        #f_code=represent block of executable pyhton code
        #co_filename contain file_name
    
class CustomException(Exception):
   def __init__(self,error_msg,error_detail:sys):
      
     super().__init__(error_msg)   
     self.error_msg=error_msg_detail(error_msg,error_detail=error_detail)
   

   def __str__(self):
      return self.error_msg

  

     