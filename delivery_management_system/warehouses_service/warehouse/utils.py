import uuid


def generate_uuid():
    """This function will be used instead of a prime number"""
    return str(uuid.uuid4())


