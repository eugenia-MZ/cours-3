import random  # module pour générer des nombres aléatoires
import string
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


"""
-----Ex 3-----
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

for key, value in dictionary.items():
    print(f"dictionary[{key}]c = {value}")

# TODO: Use a for loop with range() to print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# TODO: Use list comprehension to create a new list of squares of numbers
squares = [i**2 for i in numbers]
print(squares)

# TODO: Use a nested for loop to create a multiplication table (up to 5x5)
facteurs = [0, 1, 2, 3, 4, 5]
print("-----")
for i in facteurs:
    for j in facteurs:
        print(f"résultat de {i} x {j} : {i*j}")
"""

"""
# TODO: Use a while loop to print numbers from 1 to 10

i = 1
while i <= 10:
    print(i)
    i = i+1

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)


# le programme choisit un nombre aléatoire entre 1 et 10
nombre_secret = random.randint(1, 10)
jeu = 0

while jeu != nombre_secret:
    jeu = int(input("Entrez un nombre entre un 1 et 10 : "))
    if jeu == nombre_secret:
        print("Bien joué tu as trouvé le nombre !")
    elif jeu < 1 or jeu > 10:
        print("j'ai dit entre 1 et 10 !")
    else:
        print("Raté, essaye encore")

# TODO: Use a while loop to calculate the factorial of a number
num = int(input("Entrez un nombre pour calculer sa factorielle : "))
fact = 1
f = 1

while f <= num:
    fact = fact * f
    f = f+1

print(f"la factorielle de {num} est : {fact}")
"""


"""
-----Ex 4-----
# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)

is_finished = False
new_op = "y"

while is_finished is not True:
    while new_op == "y":
        good_numbers = True
        good_operator = True

        nb1 = int(input("Entrez un 1er nombre : "))
        nb2 = int(input("Entrez un 2e nombre : "))
        operator = input("Choisissez une opération entre +, -, *, / : ")     

        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            good_operator = False

        while good_operator is False:
            print("Choisissez un opérateur valide !")
            operator = input("Choisissez une opération entre +, -, *, / : ")
            if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                good_operator = True

        if operator == "+":
            print(f"{nb1} + {nb2} = {nb1+nb2}")

        elif operator == "-":
            print(f"{nb1} - {nb2} = {nb1-nb2}")

        elif operator == "*":        
            print(f"{nb1} x {nb2} = {nb1*nb2}")

        elif operator == "/":
            if nb2 != 0:
                print(f"{nb1} / {nb2} = {nb1/nb2}")
            else:
                print(f"La division par {nb2} est impossible")
                is_finished = True

        new_op = input("Souhaitez-vous refaire une nouvelle opération ? (y/n)" )
            
        if new_op == "n":
            is_finished = True

        while new_op != "y" and new_op != "n":
            print("Choisissez une réponse entre 'y' et 'n'")
            new_op = input("Souhaitez-vous refaire une nouvelle opération ? (y/n)")
"""

"""        
# TODO: Create a function that counts the occurrence of each vowel in a string

sentence = "je fais un master"


def count_vowel(sentence):
    vowel = "aeiouyAEIOUY"
    i = 0
    nb_vowel = 0
    for i in sentence:
        if i in vowel:
            nb_vowel += 1
        
    return nb_vowel


test = "je suis la"
print(count_vowel(test))

# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)
all_letters = string.ascii_lowercase + string.ascii_uppercase
# print(type(letters))

letter = input("Entrez une lettre : ")
decalage = int(input("Entrez un nombre de décalage : "))
start_index = all_letters.index(letter)
letters_decalage = all_letters[start_index:] + all_letters[:start_index]


def caesar_cipher(letter, decalage):
    
    j = 0
    for j in letter:
        resultat = ""
        index = all_letters.index(j)  
        new_index = (index + decalage) % len(all_letters)
        resultat += letters_decalage[new_index]

    return resultat

caesar_cipher()

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome

# Test each function with sample inputs and print the results
"""