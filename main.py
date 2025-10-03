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
