"""
-----Ex 1-----

# TODO: Create a string variable with a sentence
sentence = "C'est moi wesh"
# TODO: Convert the string to uppercase
sentence_upper = sentence.upper()
# TODO: Convert the string to lowercase
sentence_lower = sentence.lower()
# print(f"phrase : {sentence}\nmaj : {sentence_upper}\nmin : {sentence_lower}")

# TODO: Capitalize the first letter of each word

words = sentence.split()

for word in words:
    camel = word.capitalize()
    print(camel)

# TODO: Replace a word in the string
sentence_replaced = sentence.replace("moi", "lui")
print(f"phrase changée : {sentence_replaced}")

# TODO: Split the string into a list of words

# TODO: Join the list of words back into a string using a different separator
words_join = "/".join(words)
print(f"phrase avec slash : {words_join}")

# TODO: Find the position of a specific word in the string
mot = "moi"
if mot in words:
    word_position = words.index(mot)
    print(f"position de moi dans '{sentence}' : {word_position+1}")


else:
    print("ça existe pas chef")


# TODO: Check if the string starts with a specific word
mot_debut = "C'est"
mot_debut_position = words.index(mot_debut)
if mot_debut_position == 0:
    print(f"'{mot_debut}' est le 1er mot de la phrase '{sentence}'")

else:
    print(f"'{mot_debut}' n'est pas le 1er mot")

# TODO: Remove leading and trailing whitespace from a string
print(sentence.strip())
# Print the results of each operation
"""

"""
-----Ex 2-----
# TODO: Create variables for name, age, and height
name = "Mehdi"
age = 26
height = 1.70

# TODO: Use the .format() method to create a sentence with these variables
phrase = "Je m'appelle {0}, j'ai {1} ans, et je mesure {2}m".format(name, age, height)
print(phrase)

# TODO: Use f-strings to create the same sentence
phrase_fstring = f"Je m'appelle {name}, j'ai {age} ans, et je mesure {height}m"
print(phrase_fstring)

# TODO: Use the % operator for string formatting
phrase_percent = "Je m'appelle %s, j'ai %d ans, et je mesure %.1fm" % (name, age, height)
print(phrase_percent)

# TODO: Format a float number to display only two decimal places
decimal = 3.14328738
print("%.2f" % decimal)

# TODO: Create a table-like output using string formatting
table = [name, age, height]
print("{:<10} {:<5} {:<6.2f}".format(name, age, height))
# Print all formatted strings
"""

# TODO: Create a list of numbers
numbers = [24, 52, 37.8, 4]

# TODO: Use a for loop to print each number in the list
for i in numbers:
    print(i)

# TODO: Use a for loop with enumerate() to print both index and value
for i in enumerate(numbers):
    print(i)

# TODO: Create a dictionary and use a for loop to print all keys and values
dictionary = {
    "name": "Mehdi",
    "age": 26,
    "height": 1.70,
}

# TODO: Use a for loop with range() to print numbers from 1 to 10

# TODO: Use list comprehension to create a new list of squares of numbers

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)
