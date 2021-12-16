# -*- coding: UTF-8 -*-

class StatusCode:
    """
    Defines the codes and messages for standardization of communication
    """

    class SUCCESS:
        def code():
            return 1
        def message(msg=None):
            base_msg = "[SUCCESS] "
            return base_msg + msg if (msg) else base_msg.strip()

    class DUPLICATE_KEY:
        def code():
            return 2
        def message(msg=None):
            base_msg = "[DUPLICATE_KEY] "
            return base_msg + msg if (msg) else base_msg.strip()

    def find_msg_by_code(code):
        if (code == StatusCode.SUCCESS.code()):
            return StatusCode.SUCCESS.message()
        elif (code == StatusCode.DUPLICATE_KEY.code()):
            return StatusCode.DUPLICATE_KEY.message()
        return None
