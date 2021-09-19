import random


def main():
    choices = ["goat", "goat", "car"]
    random.shuffle(choices)
    # there are 3 doors randomally containing a winning car and two goats
    goat_indexes = []
    car_index = ""
    # get the goats indexes
    for j in range(len(choices)):
        if choices[j] == "goat":
            goat_indexes.append(j)
        else:
            car_index = j
    # the guest chooses a door
    first_choice_index = random.randint(0, 2)
    # the host chooses a door containing a goat and open it
    if first_choice_index == car_index:
        open_door = random.choices(goat_indexes)[0]
    else:
        open_door = goat_indexes[1] if goat_indexes[0] == first_choice_index else goat_indexes[0]
    goat_indexes.remove(open_door)
    # choose the second choice
    second_choice_index = goat_indexes[0] if first_choice_index == car_index else car_index
    return second_choice_index == car_index


success = 0
count = 1000000  # the bigger the better
for i in range(count):
    if main():
        success += 1
fraction = success / count
print("probability = ", fraction, " = ", fraction * 100, " %")
# as you see, the probability that the second door contains the winning car is 2/3
