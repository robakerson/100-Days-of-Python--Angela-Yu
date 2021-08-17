# robot maze, follow right wall
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#first two loops ensure seeding doesn't leave robot in infinite square pattern with no wall on the right
while right_is_clear() & front_is_clear():
    move()
while right_is_clear():
    turn_right()

#run forever until we find the exit
while at_goal()==False:
    # if there is no wall at the right, turn right and go
    if right_is_clear():
        turn_right()
        move()
    # if there is a wall at the right and space to go forward, move forward.
    else:
        if front_is_clear():
            move()
        # if there is a wall to the right and ahead, turn left and reset the loop
        else:
            turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# #jump variable number of  hurdles of variable height with variable distance between them
# def jump():
#     times_went_up = 1
#     turn_left()
#     move()
#     while right_is_clear() == False:
#         move()
#         times_went_up +=1
#     turn_right()
#     move()
#     turn_right()
#     while times_went_up > 0:
#         times_went_up-=1
#         move()
#     turn_left()
#
# # if not at goal, check ahead, move if clear, otherwise jump
# while at_goal()==False:
#     if front_is_clear() == True:
#         move()
#     else:
#         jump()



#
# # robot solve hurdle problem given unknown hurdle locations
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# # check if we are at goal
# while at_goal()==False:
#     # check if there is a wall in front of us. If yes, jump. If not, move
#     if front_is_clear() == True:
#         move()
#     else:
#         jump()

# # define and call a function
# def my_function():
#   print("Hello")
#   print("Bye")
# my_function()
