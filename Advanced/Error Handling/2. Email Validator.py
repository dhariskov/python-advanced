class NameTooShortError(Exception):
    """Name must be more than 4 characters"""

    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(message)


class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(message)


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    def __init__(self, message="Domain must be one of the following: .com, .bg, .org, .net"):
        self.message = message
        super().__init__(message)


while True:
    email = input()
    if email == "End":
        break
    name = email.split("@")[0]
    domain = email.split(".")[-1]
    if len(name) <= 4:
        raise NameTooShortError()

    if "@" not in email:
        raise MustContainAtSymbolError()

    if domain not in ["com", "bg", "net", "org"]:
        raise InvalidDomainError()

    print("Email is valid")
