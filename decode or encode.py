message = input("Enter a message to encode or decode: ")
message = message.upper()
output = ""
answer = None
for letter in message:
    if letter.isupper():
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Output message:", output)
answer = input("Hit any key to quit.")
if answer == answer:
    print("Good bye!")
   

    
