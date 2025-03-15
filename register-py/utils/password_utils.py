import hashlib

def hash_password(password):
    """
    Hash a password using MD5 (for compatibility with the existing system)
    Note: MD5 is not secure for new systems, but we're using it for compatibility
    """
    return hashlib.md5(password.encode()).hexdigest()