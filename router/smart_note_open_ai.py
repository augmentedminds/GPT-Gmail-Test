import openai
openai.api_key = "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"
openai.organization = "org-iozfEO4nyJxViFRZAAxsHfTC"
from quick_reply_prompt import Quick_reply_prompt
from long_message_prompt import Long_message_prompt


class Smart_note_open_ai(object):
    def __init__(self):
        self.openai = openai
        self.quick_reply_prompt = Quick_reply_prompt()
        self.long_message_prompt = Long_message_prompt()

    def create_quick_reply_prompt(self, email_thread ):
        prompt = self.quick_reply_prompt.return_quick_reply() + email_thread + " <stop-p>"  
        return prompt  


    def create_long_message_prompt(self, user_input, original_message ):
        prompt = self.long_message_prompt.return_long_message(user_input, original_message)
        return prompt


    def get_quick_prompt(self, document):
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=self.create_quick_reply_prompt(document),
        temperature=0.0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["<stop-p>", "<stop-r>"]
        )
        return response
    
    def get_long_message(self, user_input, original_message):
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=self.create_long_message_prompt(user_input, original_message),
        temperature=0,
        max_tokens=3300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["<stop-p>","<stop-r>"]
        )
        return response

