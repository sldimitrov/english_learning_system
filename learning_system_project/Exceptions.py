class NameTooShortError(Exception):
    pass


class DomainWithoutDotError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class DomainMustContainsDot(Exception):
    pass


class EmailHasBeenAlreadyUsedError(Exception):
    pass


class EmailDoesNotContainsAtSymbolError(Exception):
    pass
