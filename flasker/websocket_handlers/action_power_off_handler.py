
import os

from .message_handler import MessageHandler


class NormalPrintHandler():

    def __init__(self):
        self.role = r'normal_print'

    def apply_handler(self, message):
        from pudb import set_trace; set_trace()
        assert 1 == 1
