import string
lowercase_alphabets = list(string.ascii_lowercase)
ascii_value = [ord(i) for i in lowercase_alphabets]
# ord is used to convert alphabhet to its corresponding value
# ord accepts only one element

result = {k: v for k, v in zip(lowercase_alphabets, ascii_value)}
print(result)
