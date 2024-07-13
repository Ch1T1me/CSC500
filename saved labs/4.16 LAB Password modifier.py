word = input()
password = ''

# adding the boundaries
letter_map = {
        'i': '!',
        'a': '@',
        'm': 'M',
        'B': '8',
        'o': '.'
    }

# iterate through each letter in the input word
for letter in word:
    # if letter is in dictionary, replace it with the mapped character
    if letter in letter_map:
        password += letter_map[letter]
    else:
        password += letter
        
# append 'q*s' to the end of the modified password
password += 'q*s'

# output modified password
print(password)