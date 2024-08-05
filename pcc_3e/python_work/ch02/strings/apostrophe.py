# "'" valid -> "" can contain any number of '
# '"' valid -> '' can contain any number of "
# """ not valid -> "" cannot contain unescaped "
# ''' not valid -> '' cannot contain unescaped '
message = "One of Python's strengths is its diverse community."
print(message)
print("'")
print('"')
print("\"")
print('\'')