from .models import Logs

def check_status_len(status):
    if len(str(status)) == 3:
        return True
    else:
        return False
