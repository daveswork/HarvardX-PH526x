import string

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

#encryption_key = 3

#encoding = dict([(alphabet[i],(i+encryption_key)%27) for i in range(27)])


message = "hi my name is caesar"

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    encoding = dict([(alphabet[i],(i+encryption_key)%27) for i in range(27)])
    encoded = ""
    for letter in message:
        encoded += alphabet[encoding[letter]]
    return encoded

encoded_message = caesar(message, 3)
print(encoded_message)
