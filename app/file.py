class File:
    """
    duration: Time file is visible in seconds
    """

    def __init__(self, name, duration, upload_date, active=True):
        self.name = name
        self.duration = duration
        self.upload_date = upload_date
        self.active = active

    def dict(self):
        return self.__dict__
