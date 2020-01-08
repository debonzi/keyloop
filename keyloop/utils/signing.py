import hashlib


class BadSignatureError(Exception):
    """ Raised when decoded string signature doesn't match. """


def create_signed(string, secret):
    signature = hashlib.sha512("{}{}".format(string, secret).encode()).hexdigest()
    return signature + string


def retrieve_signed(signed, secret):
    value = signed[128:]
    if signed != create_signed(value, secret):
        raise BadSignatureError(
            "Signature mismatch. Ether secret is wrong or string value has been tampered"
        )
    return value
