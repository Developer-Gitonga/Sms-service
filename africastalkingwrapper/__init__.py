from . Authentication import AuthenticationService
from . SMS import SMSService


SMS = None
Authentication = None


def initialize(username, api_key):

    if username is None or api_key is None:
        raise RuntimeError('Invalid username and/or api_key')

    globals()['Authentication'] = AuthenticationService(username, api_key)
    globals()['SMS'] = SMSService(username, api_key)


