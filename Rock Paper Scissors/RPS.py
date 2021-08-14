# List of data
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# states_of_america[1] refers to Pennsylvania
# states_of_america[-1] refers to the last item in the List
# states_of_america.append("Connecticut") adds new item to the List
# states_of_america.extend(["Connecticut", "Massachusetts"]) adds 2+ items to the list


# Bill roulette program:

# # receive the names input and split into a list based on comma seperator
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# import random
# print (names)

# # length of the names list
# len(names)
# # Generate the random number that selects the bill payer
# name_selector = random.randint(0, len(names) - 1)
# # print the element of the names list corresponding to the bill payer
# print (f"{names[name_selector]} is going to buy the meal today!")


# # Treasure map program but I use math instead of position[0]
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# # convert position from str to int
# posint = int(position)
# # use math to find col and row coords
# row_coord = (posint % 10)
# col_coord = int((posint - (posint % 10))/10)
#
# # select which row from map list
# row_sel = map[row_coord-1]
# # select which column from our row and replace with X
# row_sel[col_coord - 1] = "X"
# # print the final map
# print(f"{row1}\n{row2}\n{row3}")
