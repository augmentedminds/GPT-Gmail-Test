import os

class Long_message_prompt(object):
    def __init__(self):
        pass        
    
    def return_long_message(self, user_input, original_message):
        main_prompt = "The following is an email sent to me. reply to this message in a professional manner, with the following direction " + user_input + ":\n\n" + original_message + " <stop-p>" 
        
        return main_prompt
        
        