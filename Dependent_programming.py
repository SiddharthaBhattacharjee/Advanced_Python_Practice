def validate_dict(data):
    """
    Checks if all key-value pairs in a dictionary match the name: email format.
    Returns True if all key-value pairs are valid, False otherwise.
    """
    for key, value in data.items():
        if not isinstance(key, str) or not isinstance(value, str):
            return False
        if not key.isalpha() or '@' not in value:
            return False
    return True

# Example usage
data = {'Alice': 'alice@example.com', 'Bob': 'bob@example.com', 'Charlie': 'charlie@example.com'}
result = validate_dict(data)
print(result)  # Output: True

data = {'Alice': 'alice@example.com', 'Bob': 'bob@example.com', 42: 'charlie@example.com'}
result = validate_dict(data)
print(result)  # Output: False

data = {'Alice': 'alice@example.com', 'Bob': 'bob', 'Charlie': 'charlie@example.com'}
result = validate_dict(data)
print(result)  # Output: False
