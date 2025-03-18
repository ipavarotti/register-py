import hashlib
import base64

def hash_password(password):
    """
    Hash a password using MD5 (for compatibility with the existing system)
    Note: MD5 is not secure for new systems, but we're using it for compatibility
    """
    md5_hash = hashlib.md5(password.encode()).digest()
    base64_hash = base64.b64encode(md5_hash).decode()
    return base64_hash
