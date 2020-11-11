import itertools

def ascii_sum(text):
    sum = 0
    for i in range(len(text)):
        sum += ord(text[i])
    return sum

with open("059_cipher.txt") as file:
    ciphertext = (file.read()).split(',')
    possible_keys = list(itertools.permutations(range(97,123),3))
    
    for key in possible_keys:
        message = ''
        for i in range(len(ciphertext)):
            if i%3 == 0:
                message += chr(int(ciphertext[i])^(key[0]))
            elif i%3 == 1:
                message += chr(int(ciphertext[i])^(key[1]))
            elif i%3 == 2:
                message += chr(int(ciphertext[i])^(key[2]))

        if all((word in message.lower() for word in ['a ', 'the ', ' ', 'and '])):
            print(f'''{message}\n\nThe sum of this ASCII message is {ascii_sum(message)}.''')
            break
        else:
            pass