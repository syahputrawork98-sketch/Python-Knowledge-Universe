# Menggunakan RELATIVE IMPORT untuk ke paket utils
from .utils.helper import format_msg

def authenticate(user):
    print(format_msg(f"Authenticating user: {user}..."))
    return True
