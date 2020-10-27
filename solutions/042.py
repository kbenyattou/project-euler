def t(n):
    return n*(n+1)/2

triangular_numbers = []

for i in range(100):
    triangular_numbers.append(t(i))

def word_value(w):
    value = 0
    for letter in w:
        value += ord(letter)-64
    return value

raw_words = open('042.txt', 'r')

word_list = raw_words.read().replace('\"','').split(',')

triangular_words = []

for word in word_list:
    if word_value(word) in triangular_numbers:
        triangular_words.append(word)

print(len(triangular_words))

raw_words.close()