# Coin Flip Streaks
# nie wiem czy to jest dobrze wlasciwie
import random

coin = ('T', 'H')
flips_containing_6 = 0

for j in range(10000):
    throws = []
# losowanie moneta 100 razy
    for i in range(100):
        throws.append(random.choice(coin))

    streak = 0
    previous_item = throws[0]

# sprawdzenie czy jest 6 z rzedu
    for index, item in enumerate(throws):
        if item == previous_item:
            streak += 1
            previous_item = item
            if streak == 6:
                flips_containing_6 += 1
                break
        else:
            streak = 0

print(flips_containing_6)
