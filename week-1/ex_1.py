import string

alphabet = string.ascii_letters

def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] = count_letters[letter] + 1
            else:
                count_letters[letter] = 1
    return count_letters


sentence = 'Jim quickly realized that the beautiful gowns are expensive'

address_count = counter(sentence)

most_frequent_letter = ''
max_freq = 0
for letter in address_count:
    if address_count[letter] > max_freq:
        max_freq = address_count[letter]
        most_frequent_letter = letter
print(most_frequent_letter)
