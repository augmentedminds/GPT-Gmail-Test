import os

class Quick_reply_prompt(object):
    def __init__(self):
        pass        
    
    def return_quick_reply(self):
        text = """ 
        # The following is an email sent to me. Create three quick replies that I can use to respond to this email, in an html list, which are no more then ten words each.

        # Hey, lets get together this week, how does that sound? <stop-p>

        # <ul>
        #     <li><button id="button_1">That sounds great!</button></li>
        #     <li><button id="button_2">I'm busy this week, how about next week?</button></li>
        #     <li><button id="button_3">Sorry, I'm not available this week.</button></li>
        # </ul> <stop-r>
        
        # Pleasure to e-meet. This is Dana Kang leading the Global Investment Team at Krafton. We’d love to hear more about Liquid Bit and “Mythic Golf” over a call.
        # This week, we are available Wednesday 7-8pm CST (10am KST), next week our calendar is pretty open for Monday evening. 
        # Please share 3 of your preferred time slots, and we will share the zoom invitation to confirm. <stop-p>

        # <ul>
        #     <li><button id="button_1">Wed 7-8pm CST</button></li>
        #     <li><button id="button_2">Mon 7-8pm CST</button></li>
        #     <li><button id="button_3">Im not able to make it those times</button> </li> <stop-r>

        # Hello Both
        # @Matt please meet Catherine.  She's out at the moment but will be back soon.  She's honestly one of the loveliest people in games and is 
        # heading up BD for Humble (who are also seriously lovely people to work with).

        # @Catherine please meet Matt.  Matt's a top man and the CEO of Liquid Bit (they did the massively well received Killer Queen Black).
        # They've got a new game in development and it feels like a Humble Game (and they're a Humble type vibe of a team too).

        # I'm guessing it'll be a couple of weeks before you get a reply Matt but I'm sure Catherine will jump in when she's back. <stop-p>

        # <ul>
        #     <li><button id="button_1">Thanks for the intro, I'll reach out to Catherine when she's back</button></li>
        #     <li><button id="button_2">Nice to meet you Catherine</button></li>
        #     <li><button id="button_3">I'm no longer available to meet Catherine</button></li>
        # </ul> <stop-r> 
        # """
        return text