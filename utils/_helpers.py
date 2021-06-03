import six
def to_bytes(value, encoding="ascii"):
    """Converts a string value to bytes, if necessary."""

    result = value.encode(encoding) if isinstance(value, six.text_type) else value
    if isinstance(result, six.binary_type):
        return result
    else:
        raise TypeError("%r could not be converted to bytes" % (value,))