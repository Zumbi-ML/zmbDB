# -*- coding: UTF-8 -*-

from zmb_codes import StatusCode

# Helper functions
# ==============================================================================

def json_response(status_code, data=[], message=None):
    """
    Build a JSON response
    """
    if (not message):
        message = StatusCode.find_msg_by_code(status_code)
    return {"data": data, "message": message, "status_code": status_code}
