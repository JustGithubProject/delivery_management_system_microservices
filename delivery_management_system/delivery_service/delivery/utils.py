import uuid


class StatusDelivery:
    NEW = "new"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELED = "canceled"


def generate_uuid():
    """This function will be used instead of a prime number"""
    return str(uuid.uuid4())

