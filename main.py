def turn_right():
    for i in range(3):
        turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()   
    elif wall_in_front():
        turn_left():
