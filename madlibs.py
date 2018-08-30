# madlibs activity

# story: I am very ____. Today we are going out for a ____. I am inviting ____ and i hope it will be very ____.

# input
# - 2 adjectives
# - 1 verb
# - 1 noun

# output
# - outputs story with adjectives, verbs, and nouns in the correct place.

# processing
# - user_adjectives()
# - user_verb()
# - user_noun()



# CODE

print("madlibs starting")

adjective1 = input("Input an adjective: ")
adjective2 = input("Input another adjective: ")
verb = input("Input a verb: ")
noun = input("Input a noun: ")

print("Here is your story")
print("I am very " + adjective1 + ". Today we are going out for a " + verb + ". I am inviting " + noun + " and I hope it will be very " + adjective2 + ".")



