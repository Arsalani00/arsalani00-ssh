def csv_text(value):
    result = '"'
    for character in value:
        if character == '"':
            result += '"'
        result += character
    return result + '"'
