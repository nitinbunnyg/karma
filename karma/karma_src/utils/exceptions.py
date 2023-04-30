class karmaException(Exception):
    """karma base exception class"""

    def __init__(self, message='karma Base Exception'):
        self._message = message

    def __str__(self):
        return self._message


class FuzzerException(karmaException):
    def __init__(self, message='Fuzzer Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class HostHandlerException(karmaException):
    def __init__(self, message='Host Handler Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class ScannerException(karmaException):
    def __init__(self, message='Scanner Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class WAFException(karmaException):
    def __init__(self, message='WAF Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class RequestHandlerException(karmaException):

    def __init__(self, message='RequestHandler Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class RequestHandlerConnectionReset(RequestHandlerException):

    def __init__(self, message='Connection Reset'):
        super().__init__(message)

    def __str__(self):
        return self._message


class WebAppScannerException(karmaException):
    def __init__(self, message='Web Application Scanner Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message


class WebServerValidatorException(karmaException):
    def __init__(self, message='Web Server Validator Exception'):
        super().__init__(message)

    def __str__(self):
        return self._message
