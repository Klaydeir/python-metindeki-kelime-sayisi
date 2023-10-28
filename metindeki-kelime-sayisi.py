import string

def is_word(text):
    for char in text:
        if not char in string.punctuation:
            return True
    return False

def word_count(value, output = 0):
    potential_words = value.split(" ")
    
    for word in potential_words:
        if is_word(word):
            output += 1
    
    return output

text = input("Tell something: ")
print("Total words: {}".format(word_count(text)))