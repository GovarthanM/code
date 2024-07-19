def length_of_last_word(s):
    return len(s.strip().split(' ')[-1])
s = "Hello World"
print(length_of_last_word(s))
