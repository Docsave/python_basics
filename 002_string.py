my_sentence = "Python is fun and powerful!"
print("Length of string:", len(my_sentence))
print("First character:", my_sentence[0])
print("Substring:", my_sentence[10:])
print("Lowercase:", my_sentence.lower())
print("Count of 'o':", my_sentence.count('o'))
print("Index of 'fun':", my_sentence.find('fun'))
new_message = my_sentence.replace("powerful","amazing")
print(new_message)
new_message = "Learning Python is Exciting!"
concat_plus = my_sentence + " " + new_message
print( concat_plus)
concat_format = "{} {}".format(my_sentence, new_message)
print(concat_format)
concat_fstring = f"{my_sentence} {new_message}"
print(concat_fstring)
print(dir(my_sentence))

