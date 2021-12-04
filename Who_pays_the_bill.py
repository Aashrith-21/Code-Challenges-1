# Random name generator :-) sucker who will pay for the meal
names = input("Name the bunch of friends going out for a meal\n")

# Split the above in to a list
name_list = names.split(", ")

# Print them suckers names
print(name_list)

# Lets pick the sucker who has to pay ,,, buhahahhahahahaaaa
import random
x = len(name_list)
random_list = random.randint(1, x-1)
who_pays = name_list[random_list]
print(f"{who_pays} is the idiot who pays for the meal")
