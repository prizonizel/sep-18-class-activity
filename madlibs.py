import random
#%%
noun = ["rock","paper","scissors"]
verb = ["crush","cover","cut"]
for x in range(5):
    print("Me and my friends decided to use " + noun[random.randint(0,2)] + " to " + verb[random.randint(0,2)],noun[random.randint(0,2)])


#%%
