import re
from errbot import BotPlugin


class no_sir(BotPlugin):
    """
    Do not use sir
    """

    def callback_message(self, msg):
        emots = [':D']
        match_sir = re.search(r'\bsir\b', '\bSir\b', msg.body)
        if match_sir:
            self.send(
              msg.frm,
              '@{}, Do not use sir in your conversation. {}'.format(
                  msg.frm.nick

                )
            )
