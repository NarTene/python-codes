# This program allows a user to select a language between French or Spanish to translate an English word to.
# The program takes a word in English from the user as an input and translates it to French or Spanish based 
# on language selected.  

#create a dictionary my_dictionary with two nested dictionaries english_to_french and english_to_spanish
my_dictionary = {
    "english_to_french" : {
    "car" : "voiture",
    "work" : "travail",
    "home" : "domicile",
    "father" : "pere",
    "mother" : "mere",
    "boy" : "garcon",
    "girl" : "fille",
    "money" : "argent",
    "school" : "ecole",
    "prune" : "prune"
  },
  "english_to_spanish" : {
    "car" : "coche",
    "work" : "trabajar",
    "home" : "hogar",
    "father" : "padre",
    "mother" : "madre",
    "boy" : "chico",
    "girl" : "chica",
    "money" : "dinero",
    "school" : "escuela",
    "prune" : "ciruela pasa"
  }
}

# select language to translate to: f for French, s for Spanish
select_language = input(" enter f to translate from english to French, s to translate from english to spanish:\n").lower()

# if language is French
if select_language == "f":
    input_word = input("Give me a word in English to translate in French\n").lower()
    english_to_french_w = my_dictionary["english_to_french"].get(input_word)
    # checking if the English word exists in the dictionary
    if english_to_french_w != None:
        print(f"The French translation is: {english_to_french_w}")
    else:
        # if word does not exist in the dictionary, print word is not in my memory
        print(f"{input_word} is not in my memory")


# if language is Spanish
elif select_language == "s":
    input_word = input("Give me a word in English to translate in Spanish\n").lower()
    english_to_spanish_w = my_dictionary["english_to_spanish"].get(input_word)
    # checking if the English word exists in the dictionary
    if english_to_spanish_w != None:
        print(f"The spanish translation is: {english_to_spanish_w}")
    else:
        # if word does not exist in the dictionary, print word is not in my memory
        print(f"{input_word} is not in my memory")


# print your language does not exist in my dictionary
else:
    print(f"Your language {select_language} does not exist in my dictionary")