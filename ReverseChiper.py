#Reverse Cipher
# This is the first test for reverse cipher, The program ask for a message and reverses it

message = input('Enter Message:')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
