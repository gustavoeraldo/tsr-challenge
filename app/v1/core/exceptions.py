class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EntityNotFoundError(CustomException):
    def __init__(self, message: str):
        super().__init__(message)


class EntityCreationError(CustomException):
    def __init__(self, message: str):
        super().__init__(message)
