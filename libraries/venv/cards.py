import random
random.seed(1)
cards=["jack","queen","king"]
print(random.choices(cards, weights=[25,25,25], k=3))
