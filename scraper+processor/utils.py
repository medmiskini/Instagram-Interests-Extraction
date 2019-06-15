def deemojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def list_to_string(lt):
    return ' '.join(lt)
