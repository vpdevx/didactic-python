# string  concatenation (aka(Also known as) how to put strings together)
# suppose we want to create a string that says "subscribe to _______"
# youtuber = "Test"

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Insert verb 1: ")
verb2 = input("Insert verb 2: ")
famous_person = input("Insert a famous person: ")

madlib = f"Computer programming is so {adj}! IT makes me so excited all the time because \
        I love to {verb1}. Stay hydrated and {verb2}  like you are {famous_person}"

print(madlib)